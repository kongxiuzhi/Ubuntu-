#coding:utf-8

import re

part_l = re.compile(r'((")([css|js|fonts|images]+/.*?)("))')

with open('/home/py3env/mysite/blog/templates/blog/blogbase.html','r') as f:
	fdata = f.read()

def sub_html(match):
	return '\"{% static ' + "\'"+ match.group(3) +"\'" +'%}\"'
data = part_l.sub(sub_html,fdata)
with open('/home/py3env/mysite/blog/templates/blog/baseblog.html','w') as f:
	print(data,file = f)

