# Name: Laser Nite
# MIT Username: nite
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word  = get_word()
letters_guessed = []
joined_guessed = []


def guesses():
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed
    global joined_guessed
    
    # Make list of guessed letters and dashes
    guessed_list = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_list.append(secret_word[secret_word.index(letter)])
        else:
            guessed_list.append("-")
            
    # Join the list entries together into a string of letters and dashes and print it
    joined_guessed = join(guessed_list, "")
    print joined_guessed

                        
def play_hangman():    
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    global joined_guessed
    
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    
    # Show number of letters to player as dashes
    print "\n"
    guesses()
    print "\n"
    
    # When 6 mistakes have been made, the game is over
    while mistakes_made < 6:
        # Get guess from user and make lowercase
        guess = raw_input("Enter a letter to guess: ").lower()
        print ""
        
        # Response to repeat guess of letter in secret word
        if guess in letters_guessed and guess in joined_guessed:
            print "Letter already guessed \n"
            print "Letters guessed are: " + join(letters_guessed, " ") + "\n"
            
        # Response to repeat guess of letter not in secret word
        elif guess in letters_guessed:
            # Reverse mistake count for incorrect letter already guessed
            mistakes_made -= 1
            print "Letter already guessed \n"

        # Add the guess to list of guesses if passes repeat checks above
        else:
            letters_guessed.append(guess)

        # Check if correct guess and render response
        # Response to correct guess
        if guess in secret_word:
            # Print Correct, Number of guesses left, and Dashes with known letters
            print "Correct Guess! " + str(6 - mistakes_made) + " guesses left!\n"
            guesses()
            print ""
            # If all letters are guessed, the player wins
            if joined_guessed == secret_word:
                print "You Win!"
                break
            print "Letters guessed are: " + join(letters_guessed, " ") + "\n"
            
        # Response to incorrect guess
        else:
            # Increase mistakes made
            mistakes_made += 1
            # Print Incorrect, Number of guesses left, Letters guessed, and Dashes/known letters
            print "Incorrect Guess!\n"
            if (6 - mistakes_made) > 0:
                print str(6 - mistakes_made) + " guesses left!\n"
                print "Letters guessed are: " + join(letters_guessed, " ") + "\n"
                guesses()
                print ""
            # Player loses if no guesses left
            else:
                print "You Lose! \n"
                print "The word was " + secret_word



