import random
import sys

card01 = random.randint(1, 11)
card02 = random.randint(1, 11)
card03 = random.randint(1, 11)
card04 = random.randint(1, 11)

deck = card01 + card02

computer = card03 + card04

print("Cards: {0}".format(deck))
print("Computer: {0}".format(computer))

def start():
    print("Do you want to play? \n Enter 'yes' to play \n Enter 'no' to draw a card")
    answer = input()
    if answer == "yes":
        play()
    elif answer == "no":
       pcdrawcard()
       drawcard()
       
def play():
    global deck
    global computer
    
    if deck > computer and deck < 22:
        win()
    elif deck == computer and computer < 22:
        tied()
    else:
        lost("You lose")

def drawcard():
    global deck
    cards = random.randint(1, 11)
    deck += cards
    if deck >= 22:
        lost("Busted")
    else: 
        print("Cards: {0}".format(deck))
        start()
        
def pcdrawcard():
    global computer
    global deck
    probability = random.randint(1, 11)
    cards = random.randint(1, 11)

    if probability == 3 or 5 or 9 or 1:
        computer += cards

    if computer >= 22:
        print("Opponent busted")
        print("Cards: {0}".format(deck))
        print("Computer: {0}".format(computer))
        sys.exit()

def win():
    global deck
    global computer
    print("You win")
    print("Cards: {0}".format(deck))
    print("Computer: {0}".format(computer))

def tied():
    global deck
    global computer
    print("You tied")
    print("Cards: {0}".format(deck))
    print("Computer: {0}".format(computer))

def lost(loseStatement):
    global deck
    global computer
    print("You {0}".format(loseStatement))
    print("Cards: {0}".format(deck))
    print("Computer: {0}".format(computer))


start()
