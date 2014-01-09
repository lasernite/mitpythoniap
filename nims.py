# Name: Laser Nite
# Kerberos: nite
# nims.py

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    ## Basic structure of program (feel free to alter as you please):

    while pile > 0:
        move1 = input("Player 1, how many stones do you take?")
        while move1 > 5 or move1 < 1:
            move1 = input("Player 1, how many stones do you take, between 1 and 5?")
        pile = pile - move1
        print pile
        if pile <= 0:
            print "Player 1, you lose!"
            return
        
        move2 = input("Player 2, how many stones do you take?")
        while move2 > 5 or move2 < 1:
            move2 = input("Player 2, how many stones do you take, between 1 and 5?")
        pile = pile - move2
        print pile
        if pile <= 0:
            print "Player 2, you lose!"
            return
    print "Game Over!"


play_nims(100,5)
