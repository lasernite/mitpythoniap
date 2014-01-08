#Rock Paper Scissors, Exercise 2.2
# Name: Laser Nite
# Kerberos: nite
# Date: 1/6/19
# homework_1.py


# Request Player 1 and Player 2 inputs, "rock, paper, or scissors"
p1 = raw_input("Player 1? ").lower()
p2 = raw_input("Player 2? ").lower()

# Define possible choices in game
choices = ["rock", "paper", "scissors"]

# Determine winner of rock, paper, scissors game
if p1 in choices and p2 in choices:
    
	# If Player 1 and 2 have same selection they tie
    if p1 == p2:
        print "Player 1 and Player 2 tie!"
        
	# If Player 1 is rock, Player 1 wins if Player 2 is scissors and loses if Player 2 is paper
    elif p1 == "rock" and p2 == "scissors":
        print "Player 1 Wins!"
    elif p1 == "rock" and p2 == "paper":
        print "Player 2 Wins!"
        
	# If Player 1 is scissors, Player 1 wins if Player 2 is paper and loses if Player 2 is rock
    elif p1 == "scissors" and p2 == "rock":
        print "Player 2 Wins!"
    elif p1 == "scissors" and p2 == "paper":
        print "Player 1 Wins!"
        
	# If Player 1 is paper, Player 1 wins if Player 2 is rock and loses if Player 2 is scissors
    elif p1 == "paper" and p2 == "scissors":
        print "Player 2 Wins!"
    elif p1 == "paper" and p2 == "rock":
        print "Player 1 Wins!"
        
	#This else statement should be impossible to activate- a bug check
    else:
        print "You have discovered a bug! Email me @ nite@mit.edu"
        
# A player entered an invalid choice 
else:
    print "Invalid selection: Choose rock, paper, or scissors."
