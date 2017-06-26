from django.contrib import admin
from spider import models
# Register your models here.
admin.site.register(models.crawler)
admin.site.register(models.User)
admin.site.register(models.mycrawler)