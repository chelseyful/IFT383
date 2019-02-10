#!/usr/bin/python
myNumber = input("Please enter a number from 1 to 10:   ")

# Did we get a number between 1 and 10?
if type(myNumber) is int and myNumber > 0 and myNumber < 11:
    
    # is the number equal to our facorite number?
    if myNumber == 8:
        print("You guessed my favorite number!")
    else:
        print("Wrong number! Try again!")

# Did we even get a number !?
elif type(myNumber) is int:
    print("You entered a number, but it was not between 1 and 10")

# Must have been something other than a number...
else:
    print("You did not enter a number")