import random
import os
from random import shuffle
suits = ('diamonds', 'clubs', 'hearts', 'spades')
cardtype = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'king', 'queen', 'jack', 'ace' )
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'king':10, 'queen':10, 'jack':10, 'ace':11 }

player_hands = []
gamestatus = True

class Card():
    def __init__(self, suit, ctype):
        self.suit = suit
        self.ctype = ctype
    def __str__ (self):
        return(self.ctype+" of "+self.suit)

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for ctype in cardtype:
                self.deck.append(Card(suit,ctype))
    def __str__(self):
        deck_items = ""
        for item in self.deck:
            deck_items+=(str(item))+', '
        return(deck_items)

#card = Card(suits[0], cardtype[0])
#print(str(card))


deck=Deck()
shuffle(deck.deck)

#print(deck)
#for item in deck.deck:
#   print(values[item.ctype])

def new_hands():
    i = 0
    newhand = []
    for p in players():
        while(i < 2):
            newhand.append(deck.deck[0])
            del(deck.deck[0])
            #print(player_hand)
            i = i+1
        player_hands.append(newhand)
        newhand = []
        i = 0
    return(player_hands)
        
#for i in new_hand():
#   print(i)

def players():
    player = int(input("how many players? -> "))
    #if(players > )
    playerlist = range(0,player)
    return(playerlist)
    
#print(players())
#print(new_hand())

def addcards():
    n = 0
    pl = 1
    for i in player_hands:
        newdeck=[]
        for x in i:
            newdeck.append(str(x))
        plyr_hit = input('player '+str(pl)+' your deck: '+str(newdeck) +' do you want to hit? y/n ->')
        
        if(plyr_hit == 'y' or plyr_hit == 'yes'):
            i = player_hands[n] + [deck.deck[0]]
            del(deck.deck[0])
            newdeck = []
            pl = pl+1
            n = n+1 
            for x in i:
                newdeck.append(str(x))
            input('your deck: '+str(newdeck)+\
                ' __press any key__' )
            os.system('clear')
def start():
    print("Blackish Jack - by:Faris Hijazi, Noah Boihem")
    while(gamestatus == True):
        #main loop
        pass
    
new_hands()
addcards()
#random comment
#print(player_hands)





















