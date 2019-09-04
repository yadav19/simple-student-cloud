#!/usr/bin/python36

import subprocess as sp

print("content-type: text/html")
print("")

dockerImageList = sp.getoutput("sudo docker images")

dockerimage = dockerImageList.split("\n")






print("""
<center>
<h2>Container as a service</h2>
</center>
<form action='CAAS-launch.py'>
<table align="center" width='80%' border='1'>
<tr>
<td>Enter ur container name :</td> 
<td><input name='cname' /></td>
</tr>

<tr>
<td>Enter ur image name :</td> 
<td>

<select name='imgname'>

""")


for i in dockerimage[1:] :
	print("<option>")
	j = i.split()
	print(j[0] + ":"  +  j[1])
	print("</option>")


print("""
</select>

</td>
</tr>


<tr>
<td>Enter Random port no. :</td>
<td><input name='portno' /></td>
</tr>

<tr>
<td><input type='submit' /></td> 
<td><input type='reset' /></td>
</tr>

</table>
</form>
""")


