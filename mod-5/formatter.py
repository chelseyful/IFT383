#!/usr/bin/python3
myChar = "?"
myString = "Chelsey"
myInt = 100
myFloat = 36.52

# example using concatination
print( "Hello, " + myString + "! You have " + str(myInt) + " new\
 messages, and $" + str(myFloat) + " in your bank account" + myChar)

# Example using formatter
print(f"Hello, {myString}, You have {myInt} new messages, and {format(myInt, '.2f')} in your bank account%c")
