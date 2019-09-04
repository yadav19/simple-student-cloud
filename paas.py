#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess

form=cgi.FieldStorage()
username=form.getvalue('username')
portno=form.getvalue('portno')
print(username,portno)
output=subprocess.getstatusoutput("sudo ansible-playbook paas.yml --extra-vars='cname={u} portno={p}'".format(u=username,p=portno))
print(output)

if output[0]==0:
	print("""
		<a href="http://192.168.43.251:{}" target='f1'>Click here to launch python</a> 
	        <dir><iframe width="100%" name='f1' ></iframe></dir>
		""".format(portno))

