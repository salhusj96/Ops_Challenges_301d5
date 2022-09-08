#!/usr/bin/env python3
#
# Script: Ops 301d5 Ops Challenge Solution 07
# Author: Jon Salhus                  
# Date of latest revision: 9/7/2022   
# Purpose: Generates all directories, sub-directories and files for a user-provided directory path.
# Import libraries

import os

# Read user input here into a variable

dir_input = input("Enter a directory name: ")

# Declaration of functions
def directory_function():
    for (root, dirs, files) in os.walk(dir_input):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

directory_function()

# End