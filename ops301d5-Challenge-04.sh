#!/bin/bash
#
# Script: Ops 301d5 Ops Challenge Solution 04
# Author: Jon Salhus                  
# Date of latest revision: 9/1/2022   
# Purpose: Launches a system menu with four options utilizing a loop and conditionals

PS3='Select option: '

select option in Hello Ping IPinfo Quit
    do
        if [[ $option = 'Hello' ]]
        then
            echo "Hello world!"
        elif [[ $option = 'Ping' ]]
        then   
            ping -c 4 127.0.0.1
        elif [[ $option = 'IPinfo' ]]
        then
            ip addr show
        else [[ $option = 'Quit' ]]
            break
        fi
    REPLY=
    done