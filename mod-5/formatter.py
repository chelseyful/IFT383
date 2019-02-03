#!/usr/bin/python
myChar = "?"
myString = "Chelsey"
myInt = 100
myFloat = 36.52

# example using concatination
print( "Hello, " + myString + "! You have " + str(myInt) + " new\
 messages, and $" + str(myFloat) + " in your bank account" + myChar)

# Example using formatter
print ("Hello, %s, You have %i new messages, and $%.2f in your bank account%c") \
    % (myString, myInt, myFloat, myChar)