#coding: UTF-8 
from django import template
register = template.Library()

@register.filter
def state(state):
	if state == "0":
		return "就绪"
	if state == "1":
		return "运行中"
	if state == "2":
		return "完成"
		
register.filter('state',state)