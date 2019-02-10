#!/usr/bin/python
print("You find yourself in a room with eight doors.")
print("Each door is numbered starting at 1.")
print("")
myDoor = input("Select a door 1-8: ")

# Example use of in as a condition
# The list used here is a predefined list; but could be a variable instead
if myDoor in (1,3,6,8):
    print("You enter door %d and emerge on a sandy beach..." % (myDoor) )
elif myDoor in (2,4):
    print("You enter door %d and are confronted by a giant troll!" % (myDoor) )
elif myDoor in (5,7):
    print("You attempt to open door %d, but it will not open..." % (myDoor) )
else:
    print("Umm... that does not appear to be a valid door number")
