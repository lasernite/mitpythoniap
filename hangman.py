# Name:
# MIT Username: 
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
secret_word = 'claptrap' # Change this 
letters_guessed = ["t", "a"]

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    # Imports global variables
    global secret_word
    global letters_guessed
    # Sets counter for verification of correct guess
    count = 0
    # Checks if a guessed letter is in the secret word, if it is, counter increases by 1
    for letter in letters_guessed:
        if letter in secret_word:
            count += 1
    # If the number of correct letters guessed is equal to the length of the word, return True
    if count == len(secret_word):
        return True
    # If it's not, the word is not correctly guessed, return False.
    else:
        return False


def print_guessed():
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed
    """
    COMMENTED OUT AS UNECESSARY
    # Set a dash for each letter in the secret word to start
    base = len(secret_word)*"-"
    # Convert base into list for manipulation
    base_list = []
    for dash in base:
        base_list.append(dash)

        """
    # Replace each dash with guessed letters
    list = []
    for letter in secret_word:
        if letter in letters_guessed:
            list.append(secret_word[secret_word.index(letter)])
        else:
            list.append("-")
    joined_list = join(list, "")
    print joined_list
                        
print_guessed()



def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######
    return None
