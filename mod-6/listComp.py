#!/usr/bin/python
myNumbers = (1,2,3,4,5,6,7,8,9,10)

# Uses a list comp to filter out any numbers that are not even
newList = [aNumber for aNumber in myNumbers if aNumber % 2 == 0]
print(newList)