#!/usr/bin/python36

import subprocess as sp

print("content-type: text/html")
print("")


print("<iframe name='cframe' width='100%' height='25%'>container console</iframe>")


print("<table align='center' width='90%' border='1'>")

print("""
<tr>
<th>Status</th>
<th>Image Name</th>
<th>Container Name</th>
<th>start</th>
<th>stop</th>
<th>Console</th>
</tr>
""")


print("<td>")
print("<a href='signupca.py'>start</a>")
print("</td>")

print("<td>")
print("<a href='signupca.py'>stop</a>")
print("</td>")

print("</tr>")


print("</table>")
