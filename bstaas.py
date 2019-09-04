#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp

form = cgi.FieldStorage()
pd_size = form.getvalue('size')

output=sp.getstatusoutput("sudo ansible-playbook bstaas.yml")
print(output)
if output[0] == 0 :
        print("Successfully provided Block-Storage to client.")
else :   
	print("error sharing block storage")

