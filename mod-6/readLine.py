#!/usr/bin/python
nameList = list()
namesFile = open("names", "r")
print(namesFile.closed)
# read until we close the file
while not namesFile.closed:
    aLine = namesFile.readline().rstrip()
    if aLine != "":
        nameList.append(aLine)
    else:
        namesFile.close()

# What did we get?
print(nameList)