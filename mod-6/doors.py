#!/usr/bin/python3
print("You find yourself in a room with eight doors.")
print("Each door is numbered starting at 1.")
print("")
myDoor = input("Select a door 1-8: ")
myDoor = int(myDoor)

# Example use of in as a condition
# The list used here is a predefined list; but could be a variable instead
if myDoor in (1,3,6,8):
    print(f"You enter door {myDoor} and emerge on a sandy beach...")
elif myDoor in (2,4):
    print(f"You enter door {myDoor} and are confronted by a giant troll!")
elif myDoor in (5,7):
    print(f"You attempt to open door {myDoor}, but it will not open...")
else:
    print("Umm... that does not appear to be a valid door number")
