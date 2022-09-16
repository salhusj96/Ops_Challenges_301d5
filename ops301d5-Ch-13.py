#!/usr/bin/env python3

# Script: Ops 301d5 Ops Challenge Solution 13
# Author: Jon Salhus                  
# Date of latest revision: 9/15/2022  
# Purpose: Performs a particular HTTP request based on user input and translates that data into somewhat plain terms

import requests
from requests import status_codes

url = input("Please insert a URL: ")

print("Select an HTTP method.")
def menu():
        options_str = ('Enter 1 for GET\n'
                        'Enter 2 for POST\n'
                        'Enter 3 for PUT\n'
                        'Enter 4 for DELETE\n'
                        'Enter 5 for HEAD\n'
                        'Enter 6 for PATCH\n'
                        'Enter 7 for OPTIONS\n'
                        'Enter 8 to exit : ')
        choice = input(options_str)
        return int(choice)

choice = menu()
if choice == 1:
    r = requests.get(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 2:
    r = requests.post(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 3:
    r = requests.put(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 4:
    r = requests.delete(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 5:
    r = requests.head(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 6:
    r = requests.patch(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 7:
    r = requests.options(url)
    c1 = r.status_code
    c2 = c1
    print(r.status_code)
    print(status_codes._codes[c2][0])
    print(r.headers)
elif choice == 8:
    print("Exiting script.")