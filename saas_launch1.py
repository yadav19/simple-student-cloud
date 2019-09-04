#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess as sp

sp.getoutput("firefox http://www.google.com")
