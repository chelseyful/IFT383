#!/usr/bin/python
from string import replace
from string import split
inputString = "First,Second,Third,Fourth\n"

# remove the newline
inputString = replace(inputString, "\n", "")
fields = split(inputString, ",")

# print the first few fields
print(fields[0])
print(fields[1])