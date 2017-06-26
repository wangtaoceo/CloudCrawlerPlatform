#coding: UTF-8 
"""crawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from spider import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^register/$', views.register,name='register'),#登陆
	url(r'^login/$', views.login,name='login'),#注册
	url(r'^logout/$', views.logout,name='logout'),#注销

	#主界面
	url(r'^overview/$', views.overview,name='overview'),
	#爬虫管理界面
	url(r'^spiderManager/$', views.spiderManager,name='spiderManager'),
	#代码编辑界面
	url(r'^codeEdit/$', views.codeEdit,name='codeEdit'),

	#无界面。成功：代码编辑界面，失败：主界面
	url(r'^createSpider', views.createSpider,name='createSpider'),	
	#无界面。返回爬虫结果
	url(r'^spiderResult/$', views.spiderResult,name='spiderResult'),
	#无界面。下载爬虫文件
	url(r'^downloadFile/$', views.downloadFile,name='downloadFile'),
	#无界面。数据发布处理
	url(r'^sqlImport/$', views.sqlImport,name='sqlImport'),
	#无界面。sql文件下载
	url(r'^sqlcreate/$', views.sqlcreate,name='sqlcreate'),
	#无界面。推荐爬虫部署
	url(r'^deploy/$', views.deploy,name='deploy'),
	#无界面。用户爬虫部署
	url(r'^DeploySpider', views.DeploySpider,name='DeploySpider'),
	#无界面。图表信息处理
	url(r'^showCharts/$', views.showCharts,name='showCharts'),
	#无界面。返回爬虫日志
	url(r'^showConsole/$', views.showConsole,name='showConsole'),
	#无界面。返回用户目录
	url(r'^dirlist', views.dirlist,name='dirlist'),
	#添加用户配置文件
	url(r'^addSetting', views.addSetting,name='addSetting'),
	#无界面。爬虫删除
	url(r'^removeSpider', views.removeSpider,name='removeSpider'),
	#无界面。打开文件
	url(r'^openfile', views.openfile,name='openfile'),
	#无界面。保存文件
	url(r'^savefile', views.savefile,name='savefile'),
	#无界面。开始爬虫
	url(r'^begin', views.begin,name='begin'),
	#无界面。停止爬虫
	url(r'^stop', views.stop,name='stop'),
	#无界面。返回爬虫状态（未使用）
	url(r'^state', views.state,name='state'),
]
