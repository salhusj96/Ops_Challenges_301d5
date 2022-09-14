#!/usr/bin/env python3

# Script: Ops 301d5 Ops Challenge Solution 09
# Author: Jon Salhus                  
# Date of latest revision: 9/14/2022  
# Purpose: Uses psutil to fetch system information

# Main

# Imports psutil to be utilized in the script
import psutil
# Plugs psutil.cpu_times into a variable to be manipulated
infoutput = psutil.cpu_times()
# Takes the output of cpu_times and formats it into a paired list
output_list = [["User Mode Time", infoutput[0]], ["Kernal Time", infoutput[2]], ["Idle Time", infoutput[3]], ["Priority Mode Time", infoutput[1]], ["I/O Wait Time", infoutput[4]], ["HW Interrupt Time", infoutput[5]], ["SW Interrupt Time", infoutput[6]], ["Virtual OS Time", infoutput[7]], ["Guest Virtual OS Times", infoutput[8]]]
# Takes that list and prints each item pair into a readable format
for pair in output_list:
    print(pair[0] + ": " + str(pair[1]))

# End