#!/usr/bin/python
# Demo of list functions
from string import join

gList = list()
print( len(gList) )
gList.append("Bread")
gList.append("Dog food")
gList.append("Eggs")
print( "there are %i items in the list!" % (len(gList)))
gList.remove("Bread")
print( "removed bread; there are now %i items in the list!" % (len(gList)))
print( join(gList, "\n") )