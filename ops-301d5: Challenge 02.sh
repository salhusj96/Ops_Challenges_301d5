#!/bin/bash
#
# Script: Ops 301d5 Ops Challenge Solution 02
# Author: Jon Salhus                  
# Date of latest revision: 8/30/2022   
# Purpose: Copies syslog file and appends the filename with the current date

# Gets current date and time in a variable
now=$(date +%d.%b.%Y.%H.%M.%S)
# Copies file to current working directory
cp /var/log/syslog .
# Appends the filename with the mv command using the $now variable
mv syslog syslog.$now
