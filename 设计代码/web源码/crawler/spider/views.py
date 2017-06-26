#coding: UTF-8 
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import User,crawler,mycrawler
from api import *
import sys, shutil, os, string,urllib,json,types,MySQLdb,Queue,re,safe
from django.core.urlresolvers import reverse
reload(sys)
sys.setdefaultencoding('utf8')

userdir = "userdir"
#注册
@csrf_exempt
def register(request):
	if request.method == 'POST':
		username = request.POST.get('username',"")
		password = request.POST.get('password',"")
		password2 = request.POST.get('password2',"")
		email = request.POST.get('email',"")
		if len(username) < 5:
			return render(request, "register.html",{'error':'用户名长度大于4'})
		if not re.match('^[a-zA-Z][a-zA-Z0-9_]*$',username):
			return render(request, "register.html",{'error':'用户名以字母开头，只能为数字'})
		if not re.match('^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$',email):
			return render(request, "register.html",{'error':'邮箱格式不正确','username':username,'email':email})
		if password != password2:
			return render(request, "register.html",{'error':'两次密码不一致'})
		'''
		数据验证
		'''

		serverdir = CreateScrapy(username)
		try:
			User.objects.create(username=username,password=password,email=email)
		except Exception, e:
			return render(request, "register.html",{'error':'用户名重复'})
		
		request.session['username'] = username
		return HttpResponseRedirect(reverse('overview'))
	else:
		return render(request, "register.html",{'error':''})

#登陆
@csrf_exempt
def login(request):
	if request.session.get('username',False):
		return HttpResponseRedirect(reverse('overview'))	
	else:
		if request.method == 'POST':
			username = request.POST.get('username',"")
			password = request.POST.get('password',"")
			user = User.objects.get(username=username,password=password)
			if user:
				request.session['username'] = username
				return HttpResponseRedirect(reverse('overview'))
			else:
				return render(request, "login.html",{"error":"用户名或密码不正确"})
		else:
			return render(request, "login.html")

def logout(request):
	del request.session['username']
	return HttpResponseRedirect(reverse('login'))

#总揽
@csrf_exempt
def overview(request):
	username = request.session.get('username',False)
	userinfo = User.objects.get(username=username)
	crawler_info = userinfo.crawler_set.all()
	crawlerList = mycrawler.objects.all()
	spiders = ListSpider(username)
	pending = spiders.get("pending",[])
	running = spiders.get("running",[])
	finished = spiders.get("finished",[])
	crawler_info.crawler_num_now = len(running)
	doing = 0
	did = 0

	#保存finish中的spider名字
	finish = []
	for spider in finished:
		if spider["spider"] not in finish:
			finish.append(spider["spider"])


	for spider in finished:
		for crawler in crawler_info:
			if spider["spider"] == crawler.crawler_name and spider["spider"] in finish:
				crawler.status = "2" #运行完毕
				did += 1
				finish.pop()#将已计数的名字出栈
	
	for spider in running:
		for crawler in crawler_info:
			if spider["spider"] == crawler.crawler_name:
				crawler.status = "1" #运行中
				crawler.workid = spider["id"]
				doing += 1

	#request.session['userinfo'] = userinfo
	#request.session['crawler_info'] = crawler_info
	
	return render(request, "overview.html",{'userinfo':userinfo,'crawlerList':crawlerList,'crawler_info':crawler_info,'doing':doing,'did':did})
	
#创建爬虫
@csrf_exempt
def createSpider(request):
	username = request.session.get('username',False)
	userinfo = User.objects.get(username=username)
	crawler_info = userinfo.crawler_set.all()
	if request.method == 'POST':
		spiderName = request.POST.get('name',"")
		remark = request.POST.get('remark',"")
		domain = request.POST.get('domain',"domain")
		for crawlernow in crawler_info:
			if spiderName == crawlernow.crawler_name:
				return HttpResponseRedirect(reverse('overview'))
		if spiderName == "":
			return HttpResponseRedirect(reverse('overview'))
		userinfo.crawler_num += 1
		userinfo.save()
		spider=crawler(crawler_name=spiderName,user=userinfo,remark=remark,status="0")
		spider.save()
		dirname = os.path.abspath(os.path.join(sys.path[0],os.pardir,userdir,username,username))
		CreateSpider(filedir=dirname, SpiderName=spiderName, domain=domain)
		return render(request, "codeEdit.html",{'userinfo':userinfo,'spiderName':spiderName})		
	else:
		return HttpResponseRedirect(reverse('overview'))

#删除爬虫
@csrf_exempt
def removeSpider(request):
	username = request.session.get('username',False)
	userinfo = User.objects.get(username=username)
	crawlerId = request.POST.get('crawler',"")
	try:
		userinfo.crawler_set.get(crawler_id=crawlerId).delete()
		userinfo.crawler_num -= 1
		userinfo.save()
		return HttpResponse("true")
	except Exception, e:
		return HttpResponse("false")
	

#代码编辑爬虫
@csrf_exempt
def codeEdit(request):
	username = request.session.get('username',False)
	userinfo = User.objects.get(username=username)
	crawlerId = request.GET.get('crawler',"")
	spider = userinfo.crawler_set.get(crawler_id=crawlerId)
	return render(request, "codeEdit.html",{'userinfo':userinfo,'spiderName':spider.crawler_name})

#添加配置文件
@csrf_exempt
def addSetting(request):
	username = request.session.get('username',False)
	filename = request.POST.get('filename',"")
	if not filename.endswith('.py'):
		#print filename
		return HttpResponse("false")
	dirname = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username,username))
	f = file(dirname+"\\"+filename, "w")
	f.close()
	return HttpResponse("true")

#目录浏览
@csrf_exempt
def dirlist(request):
	username = request.session.get('username',False)
	dirname = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username,username))
	filename = request.POST.get('dir',dirname)
	spidername = request.POST.get('spidername',"")+'.py'
	if filename == '/':
		filename = dirname
	r=['<ul class="jqueryFileTree" style="display: none;">']
	try:
		r=['<ul class="jqueryFileTree" style="display: none;">']
		d=urllib.unquote(filename)
		for f in os.listdir(d):
			ff=os.path.join(d,f)
			if f.endswith(('.pyc','__init__.py','pipelines.py')):#文件则不显示
				continue
			if dirname not in ff:
				continue
			if 'spiders/' in ff and spidername != f:#只显示当前爬虫文件
				continue
			if os.path.isdir(ff):
				r.append('<li class="directory collapsed"><a rel="%s/">%s</a></li>' % (ff,f))
			else:
				e=os.path.splitext(f)[1][1:] # get .ext and remove dot
				r.append('<li class="file ext_%s"><a rel="%s">%s</a></li>' % (e,ff,f))
		r.append('</ul>')
	except Exception,e:
		r.append('Could not load directory: %s' % str(e))
	r.append('</ul>')
	return HttpResponse(''.join(r))

#文件打开
@csrf_exempt
def openfile(request):
	username = request.session.get('username',False)
	location = request.POST['local']
	codefile = file(location,"r")
	text = codefile.read()
	codefile.close()
	return HttpResponse(text)

#文件保存
@csrf_exempt
def savefile(request):
	username = request.session.get('username',False)
	location = request.POST['local']
	try:
		code = request.POST['code']
		print safe.safeChick(code)
		if not safe.safeChick(code):
			return HttpResponse("unsafe")
		codefile = file(location,"w")
		codefile.write(code)
		codefile.close()
		return HttpResponse("true")
	except Exception, e:
		return HttpResponse("false")
	
	

#爬虫管理
@csrf_exempt
def spiderManager(request):
	crawlerId = request.GET.get('crawler',False)
	username = request.session.get('username',False)
	userinfo = User.objects.get(username=username)
	if crawlerId:
		spider = userinfo.crawler_set.get(crawler_id=crawlerId)
		return render(request, "spiderManager.html",{'userinfo':userinfo,'crawler':spider})
	else:
		return HttpResponseRedirect(reverse('overview'))

#部署爬虫
@csrf_exempt
def DeploySpider(request):
	username = request.session.get('username',False)
	if username in ListProject():#已经部署
		deleteScrapyd(username)

	dirname = os.path.abspath(os.path.join(sys.path[0],os.pardir,userdir,username,username))
	message = Deploy(filedir=dirname,ProjectName=username)
	return HttpResponse(message)

#启动爬虫
@csrf_exempt
def begin(request):
	crawlerId = request.POST.get('crawler',False)
	username = request.session.get('username',False)
	if crawlerId:
		spider = crawler.objects.get(crawler_id=crawlerId)
		WorkId = RunSpider(username,spider.crawler_name)
		request.session[str(crawlerId)] = WorkId
		print WorkId
		if WorkId:
			#request.session[crawlerId] = WorkId
			return HttpResponse(WorkId)
		else:
			return HttpResponse("false")

#停止爬虫
@csrf_exempt
def stop(request):
	crawlerId = request.POST.get('crawler',False)
	WorkId = request.session.get(str(crawlerId),False)
	username = request.session.get('username',False)
	if crawlerId:
		spider = crawler.objects.get(crawler_id=crawlerId)
		state = StopSpider(username,WorkId)
		return HttpResponse(state)

#查看爬虫状态
@csrf_exempt
def state(request):
	crawlerId = request.GET.get('crawler',False)
	username = request.session.get('username',False)
	if crawlerId:
		spider = crawler.objects.get(crawler_id=crawlerId)
		state = StateSpider(username,spider.crawler_name)
		return HttpResponse(state)

#爬虫结果获取
@csrf_exempt
def spiderResult(request):
	username = request.session.get('username',False)
	crawlerName = request.POST.get('crawler',False)
	filedir = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username))
	file = open(filedir+"\\"+crawlerName, "r")
	content = ""
	for line in file.readlines()[0:50]:
		line = line.strip('\n')
		line = line + ','
		content += line
	file.close()
	content = "["+content+"]"
	return HttpResponse(content.replace(r"\n",""))

#文件下载
@csrf_exempt
def downloadFile(request):
	username = request.session.get('username',False)
	crawlerName = request.GET.get('crawler',False)
	filedir = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username))
	def file_iterator(file_name, chunk_size=512):
		with open(filedir+"\\"+crawlerName,"rb") as f:
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break

	the_file_name = crawlerName+".json"
	response = StreamingHttpResponse(file_iterator(the_file_name))
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

	return response

	

#推荐爬虫部署
@csrf_exempt
def deploy(request):
	crawlerName = request.GET.get('crawler',False)
	myspider = mycrawler.objects.get(spiderfile=crawlerName)
	username = request.session.get('username',False)
	userinfo = User.objects.get(username=username)
	crawler_info = userinfo.crawler_set.all()

	for crawlernow in crawler_info:#如果部署的爬虫已存在
		if myspider.spiderfile == crawlernow.crawler_name:
			return HttpResponseRedirect(reverse('overview'))

	destPath = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username,username))
	srcPath = os.path.abspath(os.path.join(sys.path[0], "myspiderdir"))
	#写入spider文件
	spiderfile = file(srcPath+"\\"+crawlerName+".py",'r')
	spiderCode = spiderfile.read().replace(r"${projectName}",username)
	spiderfile_copy = file(destPath+r"/spiders/"+crawlerName+".py",'w')
	spiderfile_copy.write(spiderCode)
	spiderfile.close()
	spiderfile_copy.close()
	#写入item文件
	itemfile = file(srcPath+"\\"+crawlerName+"item.py",'r')
	itemcode = itemfile.read()
	itemfile_copy = file(destPath+"\\items.py",'a')
	itemfile_copy.write(itemcode)
	itemfile.close()
	itemfile_copy.close()

	userinfo.crawler_num += 1
	userinfo.save()
	spider=crawler(crawler_name=crawlerName,user=userinfo,remark=myspider.remark,status="0")
	spider.save()

	if username in ListProject():#已经部署
		# num = createEgg(os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username)))
		# filedir = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,"dist"))
		# file = filedir + "project-"+str(num)+".0-py2.7.egg"
		# createVersion(eggfile=file,version_name=num)
		# return HttpResponseRedirect(reverse('overview'))
		deleteScrapyd(username)
	#未部署
	dirname = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username))
	message = Deploy(dirname,username)
	return HttpResponseRedirect(reverse('overview'))

#图表展示
@csrf_exempt
def showCharts(request):
	username = request.session.get('username',False)
	crawlerName = request.POST.get('crawler',False)
	key = request.POST.get('checked',False)
	filedir = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username))
	file = open(filedir+"\\"+crawlerName, "r")
	data = {}
	count = 0
	for line in file.readlines():
		count += 1
		try:
			line = json.loads(line)
			linekey = ""
			if type(line[key]) == type([]):
				linekey = "".join(line[key])
			else:
				linekey = line[key]
			if linekey not in data.keys():
				data.setdefault(linekey, 1)
			else:
				data[linekey] = data[linekey] + 1
		except ValueError, e:
			break
	data = json.dumps(data) 
	return HttpResponse(str(count)+"@@"+"["+data+"]")
	


#数据库自动导入
@csrf_exempt
def sqlImport(request):
	message = ""
	username = request.session.get('username',False)
	crawlerName = request.POST.get('crawler',False)
	filedir = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username))
	try:
		ip = request.POST.get('ip',False)
		port = int(request.POST.get('port',""))
		sqluser = request.POST.get('sqluser',False)
		sqlpassword = request.POST.get('sqlpassword',False)
		dbname = request.POST.get('dbname',False)
		tablename = request.POST.get('tablename',False)
		if tablename == '':
			tablename = crawlerName
	except Exception:
		return HttpResponse("参数格式有误。")

	try:
		#建立数据库连接
		db = MySQLdb.connect(host=ip,port=port,user=sqluser,passwd=sqlpassword,db=dbname,charset="utf8")
		cursor = db.cursor()
	except:
		return HttpResponse("数据库连接失败，请确认参数是否正确。")
	#cursor.execute("DROP TABLE IF EXISTS %s"%crawlerName)
	#json文件读取
	file = open(filedir+"\\"+crawlerName, "r")
	#消息返回
	
	for jsonline in file.readlines():
		sql = JsonToSql(jsonline, tablename)
		try:
			cursor.execute(sql)
			db.commit()
		except Exception,e:
			db.rollback()
			message += str(e)
			message += "\n"
		
	db.close()
	if message == "":
		return HttpResponse("更新完毕")
	else:
		return HttpResponse(message)
	
	



#sql文件下载
@csrf_exempt
def sqlcreate(request):
	username = request.session.get('username',False)
	crawlerName = request.GET.get('crawler',False)
	filedir = os.path.abspath(os.path.join(sys.path[0], os.pardir,userdir,username,username))
	file = open(filedir+"\\"+crawlerName, "r")
	sqlfile = open(filedir+"\\"+crawlerName+".sql", "wb")
	for jsonline in file.readlines():
		line = JsonToSql(jsonline,crawlerName) + "\n"
		sqlfile.write(line)
	sqlfile.close()
	def file_iterator(file_name, chunk_size=512):
		with open(filedir+"\\"+crawlerName+".sql","rb") as f:
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break

	the_file_name = crawlerName+".sql"
	response = StreamingHttpResponse(file_iterator(the_file_name))
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

	return response

#控制台信息
@csrf_exempt
def showConsole(request):
	crawlerID = request.POST.get('crawler',False)
	page = request.POST.get('page',False)
	spider = crawler.objects.get(crawler_id=crawlerID)
	workID = request.session.get(crawlerID,False)
	username = request.session.get('username',False)
	filedir = os.path.abspath(os.path.join(sys.path[0], "logs",username,spider.crawler_name))
	file = open(filedir+"\\"+workID+".log", "r")
	lineCount = 0
	listContent =[]
	pageContent = ""
	for line in file.readlines():
		lineCount += 1
		pageContent += line
		pageContent += "<br />"
		if lineCount>100:
			listContent.append(pageContent)
			lineCount = 0
			pageContent = ""
	listContent.append(pageContent)
	if page:
		return HttpResponse(listContent[int(page)-1])
	else:
		return HttpResponse(str(len(listContent))+"@@"+listContent[-1])


