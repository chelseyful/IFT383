#!/usr/bin/python3
peeps = ('Wendy','Wayne','Wallace','Waldo','Warby','William')
for peep in peeps:
    print(f"Searching for Waldo... found {peep}")
    if peep=="Waldo":
        print("Found Waldo!")
        break
