#!/bin/python3
#
# Script: Ops 301d5 Ops Challenge Solution 06
# Author: Jon Salhus                  
# Date of latest revision: 9/62022   
# Purpose: Utilizes the python library "os" to call bash operations


# import the operating system library
import os

# use the os.system to call a number of bash commands represented in variables

var0 = 'whoami'
print(var0)
os.system(var0)

var1 = 'lshw -short'
print(var1)
os.system(var1)

var2 = 'ip a'
print(var2)
os.system(var2)