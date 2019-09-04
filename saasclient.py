#!/usr/bin/python36

print("content-type: text/html")
print("")


import cgi
import subprocess as sp

form=cgi.FieldStorage()
username=form.getvalue('username')
software=form.getvalue('software')
print(username)
print(software)
saas_output=sp.getstatusoutput("sudo ansible-playbook saas.yml --extra-vars='container={0} software={1}'".format(username , software))
print(saas_output)
if saas_output[0]==0:
   print("Firefox Provided Check your Desktop")
else:
   print("Not Provided")
