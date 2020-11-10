#!/usr/bin/python3
# Creates a file containing some number of random passwords
import random

# returns a password sreing
def makePassword(aLength):
    VALID_CHARS = "ABCDEFGHIJKLMNOPabcdefghijklmnop0123456789!?@#$&*"
    result = ""
    while len(result) < aLength:
        result += VALID_CHARS[ random.randint(0, len(VALID_CHARS) - 1) ]
    return result

pCount = 2600
outFile = open("pwords.txt","w")
while pCount > 0:
    outFile.write( makePassword(8) + "\n" )
    pCount -= 1
outFile.close()
