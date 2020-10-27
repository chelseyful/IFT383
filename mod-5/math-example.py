#!/usr/bin/python3
# Demo reads stdin and does math
import math
import sys

myInput = sys.stdin.readline()
myInput = eval(myInput)
print(myInput * math.pi)
