#!/usr/bin/env python3

# Script: Ops 301d5 Ops Challenge Solution 09
# Author: Jon Salhus                  
# Date of latest revision: 9/12/2022   
# Purpose: Loads user input into an if statement and prints relative information

# Main

magic_number = 75
user_input = input("Guess the magic number: ")
user_input = int(user_input)

if user_input == magic_number:
    print("You got it! Woohoo!")
elif user_input <= 50:
    print("Too low, try again.")
elif user_input >= 100:
    print("Too high, try again.")
elif user_input < magic_number:
    print("A little too low, try again.")
elif user_input > magic_number:
    print("A little too high, try again.")

if user_input != magic_number:
    print("Incorrect number.")

# End
