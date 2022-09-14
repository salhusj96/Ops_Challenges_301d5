#!/usr/bin/env python3

# Script: Ops 301d5 Ops Challenge Solution 09
# Author: Jon Salhus                  
# Date of latest revision: 9/13/2022   
# Purpose: Creates a new file, writes three lines to that file, prints the first line, then deletes the file

# Main

import os

myfile = open("myfile.txt", "w")
lines = ["Line 1\n", "Line 2\n", "Line 3"]
myfile.writelines(lines)
myfile.close()

myfile = open("myfile.txt", "a")
myfile.write("\n")
myfile.write("Line 4")
myfile.close()

myfile = open("myfile.txt")
print(myfile.readline())
myfile.close()

os.remove("myfile.txt")