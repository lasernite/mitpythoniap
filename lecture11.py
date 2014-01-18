######## Lecture 11 ########

## Simulations ##

# 1. Define a function that runs a single trial
#       of your simulation.
# 2. Call the function as many times as necessary,
#       saving any needed values.
# 3. Do something with the data - average it out,
#       make a graph, etc.

import random

def rollDie():
    """Returns a value from 1 to 6, inclusive,
    representing the face of the die that was
    rolled."""
    return random.choice([1,2,3,4,5,6])

def runDieTrial(numTrials):
    """Runs a die-rolling simulation numTrials
    times and returns the arithmetic mean of the
    rolls.
    numTrials: int representing the number of trials
    returns: a float representing the mean value of
        the roll"""
    total = 0
    for trial in range(numTrials):
        total += rollDie()
    # note that float isn't around the whole quantity
    return total/float(numTrials)


print '5', runDieTrial(5)
print '50', runDieTrial(50)
print '500', runDieTrial(500)
print '5000', runDieTrial(5000)
print '50000', runDieTrial(50000)

def runDiceTrial(numDice, numTrials):
    """Runs a dice-rolling simulation numTrials
    times with numDice dice and returns the
    arithmetic mean of the rolls.
    numTrials: int representing the number of trials
    numDice: int representing the number of dice
    returns: a float representing the mean value of
        the roll"""
    total = 0
    for trial in range(numTrials):
        for die in range(numDice):
            total += rollDie()
    # note that float isn't around the whole quantity
    return total/float(numTrials)

print runDiceTrial(1, 5000)
print runDiceTrial(3, 5000)




class Die():
    """Represents a die."""
    
    def __init__(self, numSides):
        """Creates a die object.
        numSides: an int representing the number of
            sides on the die."""
        self.numSides = numSides

    def roll(self):
        """Simulates a roll of the die by returning
        an integer value.
        returns: int between 1 and numSides, inclusive"""
        # chooses a number from [1,2,3,4, ... numSides]
        return random.choice(range(1, self.numSides + 1))

# Uncomment the following two methods to see the class
# instances print nicely
        
##    def __str__(self):
##        # Use return, not print!
##        return "Die with " + str(self.numSides) + " sides"
##
##    def __repr__(self):
##       return self.__str__() 

def runDiceObjectTrial(numDice, numTrials):
    """Runs a dice-rolling simulation numTrials
    times with numDice 6-sided dice and returns the
    arithmetic mean of the rolls.
    numTrials: int representing the number of trials
    numDice: int representing the number of dice
    returns: a float representing the mean value of
        the roll"""
    total = 0
    # Run the simulation numTrials times
    for trial in range(numTrials):
        # Create dice instances; store them in a list
        diceList = []
        for dieNum in range(numDice):
            diceList.append(Die(6))
        for die in diceList:
            total += die.roll()
    # note that float isn't around the whole quantity
    print diceList
    return total/float(numTrials)

print runDiceObjectTrial(1, 5000)
print runDiceObjectTrial(3, 5000)
