#!/usr/bin/python3
#import string

# Define a small dictionary
acronyms = {
    "UTO":"University Technology Office",
    "EAS":"Engagement and Advising Services",
    "TPS":"The Polytechnic School",
    "GNU":"GNU is Not UNIX",
    "OSD":"Operating System Deployment"
}

# Display a list of keys and ask the user which one they would like to see
keyList = "\n".join(acronyms.keys())
print(keyList)
selection = input("Please enter one of the entries above to see definition")

# Generate and print key and associated value
outputString = "\n%s\n\t%s\n" % (selection.upper(),acronyms[selection.upper()])
print(outputString)
