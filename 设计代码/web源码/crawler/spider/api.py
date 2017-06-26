#coding: UTF-8 
import sys,os,re,json,types
from scrapyd_api import ScrapydAPI
reload(sys)
sys.setdefaultencoding('utf8')


userdir = "userdir"
scrapyd = ScrapydAPI('http://localhost:6800')

# 用户目录创建
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

#创建用户爬虫项目
def CreateScrapy(username):
	pwd = sys.path[0]
	dirname = os.path.abspath(os.path.join(pwd, os.pardir,userdir,username))
	mkdir(dirname)
	os.chdir(dirname)
	cmd = "scrapy startproject " + username
	message = os.system(cmd)
	scrapydir = dirname+"\\"+username
	isExists = os.path.exists(scrapydir)
	if isExists:
		return scrapydir
	else:
		return False

#创建爬虫文件
def CreateSpider(filedir,SpiderName,domain):
	os.chdir(filedir)
	cmd = "scrapy genspider -t crawl %s %s" % (SpiderName,domain)
	message = os.system(cmd)
	if message == 0:
		return True
	else:
		return False

#将爬虫部署到scrapyd
def Deploy(filedir,ProjectName,DeployName="scrapyd"):
	os.chdir(filedir)
	fp = file(filedir+"\\scrapy.cfg","w")
	content = '''# Automatically created by: scrapy startproject
#
# For more information about the [deploy] section see:
# https://scrapyd.readthedocs.org/en/latest/deploy.html

[settings]
default = %s.settings

[deploy:%s]
url = http://localhost:6800/
project = %s
	''' % (ProjectName,DeployName,ProjectName)
	fp.writelines(content)
	fp.close()
	cmd = "scrapyd-deploy %s -p %s" % (DeployName,ProjectName)
	message = os.system(cmd)
	return message

#删除某一工程
def deleteScrapyd(projectName):
	flag = scrapyd.delete_project(projectName)
	return flag

#创建一个新版本
# def createVersion(eggfile,version_name,project_name="project"):
# 	egg = open(eggfile,"rb")
# 	spidernum = scrapyd.add_version(project_name, 'r'+str(version_name), egg)
# 	egg.close()
# 	flag = scrapyd.delete_version(project_name, 'r'+str(version_name-1))
# 	return spidernum

# #创建egg文件,文件生成在当前目录dist文件夹中，返回版本号
# def createEgg(workdir):
# 	os.chdir(workdir)
# 	configflie = open("setup.py","r+")
# 	config = configflie.read()
# 	matchObj = re.search( r"version      = '(.*?).0'",config)
# 	version = int(matchObj.group(1))
# 	version += 1
# 	substring = "version      = '%s.0'," % str(version)
# 	config = re.sub('version.*', substring, config)
# 	configflie.seek(0)
# 	configflie.write(config)
# 	configflie.close()
# 	cmd = "python setup.py bdist_egg"
# 	message = os.system(cmd)
# 	return version

#运行爬虫
def RunSpider(ProjectName,SpiderName):
	spiders = ListSpider(ProjectName)
	running = spiders["running"]
	for spider in running:
		if spider["spider"] ==  SpiderName:
			return False

	SpiderId = scrapyd.schedule(ProjectName, SpiderName)
	return SpiderId

#停止爬虫 state:'running' or 'pending'.
def StopSpider(ProjectName,SpiderId):
	state = scrapyd.cancel(ProjectName, SpiderId)
	return state

#查看爬虫状态
def StateSpider(ProjectName,SpiderId):
	state = scrapyd.job_status(ProjectName, SpiderId)
	return state

#查看项目下所有爬虫，返回json
def ListSpider(ProjectName):
	try:
		SpiderJson = scrapyd.list_jobs(ProjectName)
		return SpiderJson
	except Exception, e:
		return {}
	

#查看所有项目
def ListProject():
	return scrapyd.list_projects()

#json转sql(插入语句)
def JsonToSql(jsonline,tableName):
	data = json.loads(jsonline)
	keyString = ""
	valueString = ""
	for key,value in data.items():
		if type(value) == type([]):
			 value = "".join(value)
		keyString = keyString + key
		keyString = keyString + ","
		valueString = valueString + "'"
		valueString = valueString + value
		valueString = valueString + "',"
	keyString = keyString[:-1]
	valueString = valueString[:-1]
	sql = "insert into %s (%s) values (%s);" % (tableName,keyString,valueString)
	return sql



if __name__ == '__main__':
	print CreateScrapy("qwe")
	#CreateSpider(dir,"spider","123")
	#DeploySpider(r"E:\graduation\code\crawler\userdir\111\spider1","spider1")
	#print RunSpider("spider1", "spider")
	
