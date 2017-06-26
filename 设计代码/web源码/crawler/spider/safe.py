#coding: UTF-8 
'''
爬虫代码安全审查：
检测方面：
1、爬虫文件禁止导入os，sys模块
2、爬虫文件禁止调用open，file函数

'''
import re

Regularly = [r'import(.*?)os',
r'import(.*?)sys',
r'from(.*?)os',
r'from(.*?)sys',
r'open((.*?))',
r'file((.*?))']

def safeChick(code):

	find = None

	for match in Regularly:
		find = re.search(match, code)
		if find is not None:
			return False

	return True
	

if __name__ == '__main__':
	f = open('test.py','r')
	string = f.read()
	print string
	print safeChick('test.py', string)