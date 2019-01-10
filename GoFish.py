#Go Fish: AP Computer Science Principles Project
#Made by Jack Lemm


import random #imports a package containing functions dealing with random number math

playerNum = 0 #a global variable storing the player's number of pairs
oppNum = 0 #a global variable storing the opponents's number of pairs
playerHand = [] #a global list of the integers in the player's hand
oppHand = [] #a global list of the integers in the opponent's hand

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] #a global list of every card availible in the deck

def QInt(intTest):
    """Takes a parameter and determines whether it can be converted to an int, returning true or false accordingly"""
    try: #tries to see if it can be converted without error
        int(intTest) #converts parameter to an integer
        return True #returns true if it can be converted without error
    except ValueError: #if the ValueError occurs, the parameter cannot be converted to an integer
        return False #returns true if it can be converted without error
        
        
def restart():
    """Waits for the user to input yes and then restarts by calling the deal() and game() function"""
    print("")
    print("Restart?")
    response = raw_input()
    response = response.lower() #puts input into lowercase, so that any case iteration of "yes" is accepted
    if(response == "yes"):
        print("")
        deal()
        game()
        #calls the functions responsible for starting a game
    else:
        print("*Answer with yes to restart*")
        restart() #calls restart() again to give users another chance to input "yes"
        
        
def deal():
    """Randomly initializes all of the values within the player's and opponent's hand. Also resets the global variables for when the user restarts."""
    global playerNum
    global oppNum
    global playerHand
    global oppHand
    global cards
    playerNum = 0
    oppNum = 0
    playerHand = []
    oppHand = []

    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #global variables reset for when a user restarts
    
    first = random.choice(cards)
    second = random.choice(cards)
    third = random.choice(cards)
    fourth = random.choice(cards)
    fifth = random.choice(cards)
    sixth = random.choice(cards)
    seventh = random.choice(cards)
    playerHand = [first, second, third, fourth, fifth, sixth, seventh]
    #makes a list out of random cards taken from the deck
    while(len(set(playerHand)) != len(playerHand)): #ensures all the cards are different
        first = random.choice(cards)
        second = random.choice(cards)
        third = random.choice(cards)
        fourth = random.choice(cards)
        fifth = random.choice(cards)
        sixth = random.choice(cards)
        seventh = random.choice(cards)
        playerHand = [first, second, third, fourth, fifth, sixth, seventh]
    cards.remove(first)
    cards.remove(second)
    cards.remove(third)
    cards.remove(fourth)
    cards.remove(fifth)
    cards.remove(sixth)
    cards.remove(seventh)
    #removes the cards put in the hand from the deck
    first = random.choice(cards)
    second = random.choice(cards)
    third = random.choice(cards)
    fourth = random.choice(cards)
    fifth = random.choice(cards)
    sixth = random.choice(cards)
    seventh = random.choice(cards)
    oppHand = [first, second, third, fourth, fifth, sixth, seventh]
    #makes a list out of random cards taken from the deck
    while(len(set(oppHand)) != len(oppHand)): #ensures that all the cards are different
        first = random.choice(cards)
        second = random.choice(cards)
        third = random.choice(cards)
        fourth = random.choice(cards)
        fifth = random.choice(cards)
        sixth = random.choice(cards)
        seventh = random.choice(cards)
        oppHand = [first, second, third, fourth, fifth, sixth, seventh]
    cards.remove(first)
    cards.remove(second)
    cards.remove(third)
    cards.remove(fourth)
    cards.remove(fifth)
    cards.remove(sixth)
    cards.remove(seventh)
    #removes the cards put in the hand from the deck


def game():
    """Continues the main functions of a round of Go Fish until the ending
    conditions are met"""
    global playerHand
    global oppHand
    global cards
    global playerNum
    global oppNum
    while(len(playerHand) > 0 and len(oppHand) > 0 and len(cards) > 0): #conditions for the game not to end
        playerTurn()
    print("The game is over!")
    if(playerNum == oppNum):
        print("You have tied with the opponent!")
    elif(playerNum > oppNum):
        print("You've won against the opponent!")
    elif(oppNum > playerNum):
        print("You've lost against the opponent!")
    restart()
        
        
def playerTurn():
    """The player's turn; they ask for a card from the opponent via raw_input,
    and pairs are made and calculated"""
    global oppHand
    global playerHand
    global playerNum
    global oppNum
    print("Your number of pairs: " + str(playerNum))
    print("The opponent's number of pairs: " + str(oppNum))
    print("The opponent's number of cards: " + str(len(oppHand)))
    print("Your current deck:" + str(playerHand))
    #information on the current state of the game
    print("What number between 1 and 13 do you ask for?")
    response = raw_input() #takes input for card request
    pair = False #a variable describing whether or not the new card will pair with a previous one
    has = False #a variable describing whether the opponent has the card the player is requesting
    if(QInt(response)): #if input is a viable integer
        if(int(response) >= 1 and int(response) <= 13): #if input is between 1 and 13
            for i in oppHand: #cycles through opponents hand
                if(i == response): #a card in the hand matches the requested card
                    print("The opponent hands you the card.")
                    oppHand.remove(i) #removes card from hand
                    for x in playerHand:
                        if(x == i): #the user has a pair
                            pair = True
                            print("You have a pair of " + str(x) + "s!")
                            playerHand.remove(x) #removes excess card from pair
                            playerNum += 1  #adds to pair number
                            break
                    if(pair == False):
                        playerHand.append(i) #adds card to hand
                    has = True
            if(has == False): #opponent doesn't have card
                    goFish() 
        else:
            print("*Please enter a number between 1 and 13*")
            playerTurn()
    else:
        print("*Please enter a number between 1 and 13*")
        playerTurn()
    oppTurn()
    
    
def oppTurn():
    """The opponents's turn; they ask for a card from the usre via random chance,
    and pairs are made and calculated"""
    if(len(playerHand) > 0 and len(oppHand) > 0 and len(cards) > 0): #game ending conditions, in case the player meets them during their turn    
        global oppHand
        global playerHand
        global playerNum
        global oppNum
        response = random.choice(oppHand) #randomly asks for one of their cards to attempt to make a pair
        has = False
        print("The opponent asks for a " + str(response) + ".")
        for i in playerHand:
            if(i == response):
                print("You give it to them.")
                playerHand.remove(i) #takes card from player's hand
                for x in oppHand:
                    if(x == i): #opponent has a pair
                        pair = True
                        print("The opponent has a pair of " + str(x) + "s!")
                        oppHand.remove(x) #removes excess card
                        oppNum += 1  #increases opponent's number of pairs
                        break
                if(pair == False):
                    playerHand.append(i)
                has = True
        if(has == False): #user doesn't have the requested card
            print("You don't have one.")
            goFishOpp()              


def goFishOpp():
    """Same as goFish(), but pertains to the opponent's cards"""
    global oppNum
    global oppHand
    global cards
    pair = False
    print("Go fish!")
    card = random.choice(cards)
    cards.remove(card)
    print("The opponent picks a card from the deck.") 
    for x in oppHand:
        if(x == card):
            pair = True
            print("The opponent has a pair of " + str(x) + "s!")
            oppHand.remove(x)
            oppNum += 1  
            break
    if(pair == False):
        oppHand.append(card) 
        
        
def goFish():
    """If the opponent doesn't have the requested card, the user takes a card
    from the deck. Pairs are also made and calculated"""
    global playerNum
    global playerHand
    global cards
    pair = False
    print("Go fish!")
    card = random.choice(cards) #picks random card from deck
    cards.remove(card) #removes card from deck
    print("You pick a card and get a " + str(card)) 
    for x in playerHand:
        if(x == card): #it's a pair
            pair = True
            print("You have a pair of " + str(x) + "s!")
            playerHand.remove(x)
            playerNum += 1  
            break
    if(pair == False):
        playerHand.append(card)
                  

deal() #initiates the game
game()
        
    