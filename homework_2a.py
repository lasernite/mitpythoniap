# Name: Laser Nite
# Kerberos: nite
# Date: 1/8/14
# homework_2a.py

# **********  Exercise 3.1 **********

def rock_paper_scissors(p1, p2):
    choices = ["rock", "paper", "scissors"]
    if p1 in choices and p2 in choices:
    
	# If Player 1 and 2 have same selection they tie
        if p1 == p2:
            return "Player 1 and Player 2 tie!"
        
	# If Player 1 is rock, Player 1 wins if Player 2 is scissors and loses if Player 2 is paper
        elif p1 == "rock" and p2 == "scissors":
            return "Player 1 Wins!"
        elif p1 == "rock" and p2 == "paper":
            return "Player 2 Wins!"
        
	# If Player 1 is scissors, Player 1 wins if Player 2 is paper and loses if Player 2 is rock
        elif p1 == "scissors" and p2 == "rock":
            return "Player 2 Wins!"
        elif p1 == "scissors" and p2 == "paper":
            return "Player 1 Wins!"
        
	# If Player 1 is paper, Player 1 wins if Player 2 is rock and loses if Player 2 is scissors
        elif p1 == "paper" and p2 == "scissors":
            return "Player 2 Wins!"
        elif p1 == "paper" and p2 == "rock":
            return "Player 1 Wins!"
        
	# This else statement should be impossible to activate- a bug check
        else:
            return "You have discovered a bug! Email me @ nite@mit.edu"
        
    # A player entered an invalid choice 
    else:
        return "Invalid selection: Choose rock, paper, or scissors."

# Tests for 3.1
print rock_paper_scissors("rock","rock")
print rock_paper_scissors("paper","scissors")
print rock_paper_scissors("rock","cat")



# *********** Exercise 3.2 ***********

from math import *

## 1 - multadd function
def multadd(a, b, c):
    return a * b + c

# Test Cases
print multadd(4,5,1)
print multadd(3,3,3)
print multadd(1,2,3)


## 2 - Equations

# angle_test
angle_test = str(multadd(cos(pi/4), 0.5, sin(pi/4)))
print "sin(pi/4) + cos(pi/4)/2 is: " + angle_test

# ceiling test
ceiling_test = str(multadd(2.0,log(12,7),ceil(276/19.0)))
print """ceiling(276/19) + 2 log_7(12) is:""" + ceiling_test


## 3 - yikes function
def yikes(x):
    return multadd(x, e**-x, (1-e**-x)**0.5)

# Test Cases
num = 5
print "yikes(5) =", yikes(num)


