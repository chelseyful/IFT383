#!/usr/bin/python3

# Loop while total is zero or user has provided another number to add
myTotal = 0
myInput = 0
while myTotal == 0 or myInput != 0:
    myInput = input("Please enter a number, 0 to stop: ")
    myTotal+=myInput
print(myTotal)
