import random

card01 = random.randint(1, 11)
card02 = random.randint(1, 11)
card03 = random.randint(1, 11)
card04 = random.randint(1, 11)

deck = card01 + card02

computer = card03 + card04

print("Cards: {0}".format(deck))

def start():
    print("Do you want to play? \n Enter 'yes' to play \n Enter 'no' to draw a card")
    answer = input()
    if answer == "yes":
        play()
    elif answer == "no":
       drawcard()

def play():
    global deck
    global computer
    
    if deck > computer and deck < 22:
        win()
    elif deck == computer and computer < 22:
        tied()
    else:
        lost()

def drawcard():
    global deck
    cards = random.randint(1, 11)
    deck += cards
    if deck >= 22:
        lost()
    else: 
        print("Cards: {0}".format(deck))
        start()
        
def win():
    global deck
    print("You win")
    print("Cards: {0}".format(deck))
    print("Computer: {0}".format(computer))

def tied():
    global deck
    print("You tied")
    print("Cards: {0}".format(deck))
    print("Computer: {0}".format(computer))

def lost():
    global deck
    print("You lose")
    print("Cards: {0}".format(deck))
    print("Computer: {0}".format(computer))


start()
