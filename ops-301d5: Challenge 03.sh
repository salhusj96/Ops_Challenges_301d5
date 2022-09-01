#!/bin/bash
#
# Script: Ops 301d5 Ops Challenge Solution 02
# Author: Jon Salhus                  
# Date of latest revision: 8/31/2022   
# Purpose: Prompts user for directory input and modifies file permissions in that directory

#User input for dir
read -p "Name an existing directory: " dir_input
#User input for permissions
read -p "Set RWX permissions: " perm_input
#Navigates to the directory input by user
cd "$dir_input"
sleep 1s
#Modifies contents of current directory with previous permissions input
chmod -R $perm_input ./
#Lists the contents of the directory and their newly set permissions
ls -l
