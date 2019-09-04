#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp


form = cgi.FieldStorage()
user_name = form.getvalue('user_name')
lv_size = form.getvalue('lv_size')
print(user_name)
print(lv_size)

output=sp.getstatusoutput("sudo ansible-playbook ostaas.yml --extra-vars='user_name={u} lv_size={l}'".format(u=user_name, l=lv_size))

if output[0] == 0 :
	print("<b> NFS-server succesfully created</b>")

client_mount=sp.getstatusoutput("sudo ansible-playbook ostaasclient.yml --extra-vars='user_name={u} lv_size={l}'".format(u=user_name, l=lv_size))

if client_mount[0] == 0 :
	print("<b>Enjoy free cloud storage..</b>")

else:
	print("Sorry, We're facing technical issue. please visit after some time")
