#!/usr/bin/python3
# Demo of list functions
gList = list()
print( len(gList) )
gList.append("Bread")
gList.append("Dog food")
gList.append("Eggs")
print( f"there are {len(gList)} items in the list!")
gList.remove("Bread")
print( f"removed bread; there are now {len(gList)} items in the list!")
print( "\n".join(gList) )
