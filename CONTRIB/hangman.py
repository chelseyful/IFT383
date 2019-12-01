# Eric Richmann
# IFT 383 Term B
# Fall 2019

#importing random module
import random

#This opens the dictionary.txt file which contains all the words.
dictionary = open("dictionary.txt", "r")

# reading is used to read the lines in the dictionary file
reading = dictionary.readlines() 

# the random variable is used to create a random number that corresponds to a line in the dictionary.txt file
random = random.randint(0,58110)

# the previous reading and random variables are comined to create our secret, random word that the user will have to guess
word = reading[random]

# asking for the users name and greeting them
name = raw_input("Hello. What is your name? ")
print "Hello, " + name, "Lets play hangman!"

#creates an variable with an empty value
guesses = ''

# turn will be used to determine the turn the player has. 
turn = 10

#this while loop will run as long as the turn(s) are greater than 0
while turn > 0:         

    # starts a counter with 0 assigned
    fail = 0             

    # for loop for every character in secret word    
    for char in word:      

    # this will see if the character is in the players guess
        if char in guesses:    
    
        # prints out the character
            print char,    

        else:

        # if the letter is not found, a dash will be printed and then the fail counter will be increased by 1 
            print "_",         
            fail += 1    

    # if statement that will print the player has won if fail is equal to 0
    if fail == 0:        
        print "You have won!!!"      
        break           
    print

    # ask the user go guess a letter
    gues = raw_input("guess a letter: ")
    guess = gues.lower()
    
    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not part of the secret word, the turn counter will decrease and print wrong
    if guess not in word:       
        turn -= 1  
        print "Wrong"    
 
    # tells the player how many turns are left
        print "You have", + turn, 'more guesses' 
 
    # if the turn is equal to zero, it will print you loose
        if turn == 0:   
            print "You Loose"  