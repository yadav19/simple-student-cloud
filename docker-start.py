#!/usr/bin/python36


import subprocess as sp
import cgi

print("content-type: text/html")

form = cgi.FieldStorage()
cname = form.getvalue('x')

o = sp.getstatusoutput("sudo docker start {}".format(cname))

if o[0] == 0:
	print("location: docker-manage.py")
	print("")


else:
	print("location: docker-manage.py")
	print("")


