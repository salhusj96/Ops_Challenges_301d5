#!/bin/bash
#
# Script: Ops 301d5 Ops Challenge Solution 05
# Author: Jon Salhus                  
# Date of latest revision: 9/2/2022   
# Purpose: Clears system logs

# Main (note: script will ONLY RUN using sudo)

cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp

# End