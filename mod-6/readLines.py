#!/usr/bin/python3
namesFile = open("names", "r")
namesList = list()
if namesFile.closed == False:
    namesList = namesFile.readlines()
    namesFile.close()
print (namesList)
