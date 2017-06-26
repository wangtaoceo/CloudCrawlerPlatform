from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	username = models.CharField(max_length=20,primary_key=True)
	password = models.CharField(max_length=20)
	email = models.CharField(max_length=20)
	date = models.DateTimeField(auto_now_add=True)
	crawler_num = models.IntegerField(default=0)
	crawler_num_now = models.IntegerField(default=0)
	
	def __str__(self):
		return self.username


class crawler(models.Model):
	crawler_id = models.AutoField(primary_key=True)
	crawler_name = models.CharField(max_length=20)
	user = models.ForeignKey(User,related_name='crawler_set')
	date = models.DateTimeField(auto_now_add=True)
	remark = models.CharField(max_length=8000)
	status = models.CharField(max_length=20)
	workid = models.CharField(max_length=50)

	def __str__(self):
		return self.crawler_name


class mycrawler(models.Model):
	crawler_id = models.AutoField(primary_key=True)
	crawler_name = models.CharField(max_length=20)
	spiderfile = models.CharField(max_length=50)
	remark = models.CharField(max_length=8000)

	def __str__(self):
		return self.crawler_name
