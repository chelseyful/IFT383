#!/usr/bin/python3
inputString = "First,Second,Third,Fourth\n"

# remove the newline
inputString = inputString.replace("\n", "")
fields = inputString.split(",")

# print the first few fields
print(fields[0])
print(fields[1])
