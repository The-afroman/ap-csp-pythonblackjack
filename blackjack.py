# disclaimer too much time was spent on this terrible game
# you should probably just play with real cards or something
import random
import os
from random import shuffle
from sys import platform
suits = ('diamonds', 'clubs', 'hearts', 'spades')
cardtype = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'king', 'queen', 'jack', 'ace' )
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'king':10, 'queen':10, 'jack':10, 'ace':11 }
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

#print(deck)
#for item in deck.deck:
#   print(values[item.ctype])


def clear_screen():
    if platform == "linux" or platform == "linux2":
        # linux
        os.system('clear')
    elif platform == "darwin":
        # OS X
        os.system('clear')
    elif platform == "win32":
        # Windows
        os.system('cls')

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
#print(i)

def players():
    global playerlist
    clear_screen()
    player = int(input("how many players? -> "))
    while(player > 10):
        player = int(input("Too many players :( try again -> "))
    playerlist = range(0,player)
    return(playerlist)
    
#print(players())
#print(new_hand())

def addcards():
    pl = 1
    for ind, i in enumerate(player_hands):
        newdeck=[]
        bust = False
        for x in i:
            newdeck.append(str(x))
        plyr_hit = input('player '+str(pl)+' your deck: '+str(newdeck) +' do you want to hit? y/n ->')
        plyr_hit = plyr_hit.lower()
        while plyr_hit == 'y' or plyr_hit == 'yes':
            player_hands[ind] = player_hands[ind] + [deck.deck[0]]
            del(deck.deck[0])
            total = []
            for x in player_hands[ind]:
                total.append(x.ctype)
            vals = []
            for n in total:
                vals.append(values[n])
            if sum(vals) > 21:
                bust = True
                plyr_hit = 'n'
            newdeck = []
            #print(vals)
            #print(total)
            
            for x in player_hands[ind]:
                    newdeck.append(str(x))
            if bust == False:
                plyr_hit = input('your deck: '+str(newdeck)+\
                    ' would you like to hit again? ' )
            else:
                input('your deck: '+str(newdeck)+', You have busted press any key to continue')
        clear_screen()
        pl = pl+1
        input('press ENTER to continue')
        clear_screen()

def winner():
    for n, i in enumerate(player_hands):
        for num, x in enumerate(i): 
            i[num] = values[x.ctype]
        player_hands[n] = sum(i)
    print(player_hands)
    win = 0
    plyr = 0
    autowin = []
    awin = False
    for en, i in enumerate(player_hands):
        if i <= 21:
            if i >= win:
                win = i
                plyr = en+1
        if i == 21:
            awin = True
            autowin.append(plyr)
    if awin == True:
        for i in autowin:
            print('player '+str(i)+' got blackjack!')
    else:
        print('player '+str(plyr)+' won with a score of '+str(win))

def play_again():
    global gamestatus
    placeholder = input('would you like to play again? y/n -> ')
    if placeholder == 'y' or placeholder == 'yes':
        gamestatus = True
    else: 
        gamestatus = False

def start():
    input("Blackish Jack - by:Faris Hijazi, Noah Boihem ----- "+\
                " press ENTER to continue")

    while(gamestatus == True):
        #main loop
        global deck
        global player_hands
        player_hands = []
        deck=Deck()
        shuffle(deck.deck)
        new_hands()
        addcards()
        winner()
        play_again()

start()

















