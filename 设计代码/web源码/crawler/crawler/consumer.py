#coding: UTF-8 
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
import json,time
from spider import api

user = {}
#message.reply_channel    一个客户端通道的对象
#message.reply_channel.send(chunk)  用来唯一返回这个客户端

#一个管道大概会持续30s

#当连接上时，发回去一个connect字符串
@channel_session_user_from_http
def ws_connect(message):
	username = message.http_session.get('username',False)
	#print "connect successful"
	if username:
		message.channel_session['username'] = username
		spidersNow = api.ListSpider(username)
		message.channel_session['spidersNow'] = spidersNow
		time.sleep(2)
		user[username] = 0
		message.reply_channel.send({'text':"["+json.dumps(spidersNow)+"]"})

	

#将发来的信息原样返回
@channel_session
def ws_message(message):
	username = message.channel_session.get('username',False)
	spiders = message.channel_session.get('spidersNow',False)
	if username:
		while True:
			#print "process:"+str(user[username])
			if user[username] == 1:
				break
			spidersNow = api.ListSpider(username)
			if cmp(spidersNow, spiders) == 0:
				time.sleep(5)
			else:
				message.channel_session['spidersNow'] = spidersNow
				message.reply_channel.send({'text':"["+json.dumps(spidersNow)+"]"})
				break

#如果连接断开，终止请求
@channel_session
def ws_disconnect(message):
	username = message.channel_session.get('username',False)
	user[username] = 1
	#print "disconnect:"+str(user[username])

	
	

