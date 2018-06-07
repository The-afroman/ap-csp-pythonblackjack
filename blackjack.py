# disclaimer too much time was spent on this terrible game
# you should probably just play with real cards or something
import random
import os
from random import shuffle
from sys import platform
suits = ('diamonds', 'clubs', 'hearts', 'spades')
cardtype = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'king', 'queen', 'jack', 'ace' )
# used to reference value to card
values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'king':10, 'queen':10, 'jack':10, 'ace':11 }
gamestatus = True
# card class has two atributes suit and cards type or ctype
class Card():
    def __init__(self, suit, ctype):
        self.suit = suit
        self.ctype = ctype
    # special method used to call object as a string
    def __str__ (self):
        return(self.ctype+" of "+self.suit)
# full deck of 52 unique cards can be initialized with this class
class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for ctype in cardtype:
                # instaciated card class
                # deck made up of 52 unique instances of card class
                self.deck.append(Card(suit,ctype))
    # special method used to call object as a string
    # this method is rarely used since it will print the entire deck as a single string
    def __str__(self):
        deck_items = ""
        for item in self.deck:
            deck_items+=(str(item))+', '
        return(deck_items)

#card = Card(suits[0], cardtype[0])
#print(str(card))
#print(deck)
#for item in deck.deck:
#print(values[item.ctype])

# clears screen on all platforms
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
# uses players list to determine how many starting decks to create in player_hands
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
# uses user input to determine number of players
def players():
    global playerlist
    clear_screen()
    player = int(input("how many players? -> "))
    # ten maximum players atm
    # game can handle up to 17 player if each player decides to only draw one card
    while(player > 10):
        player = int(input("Too many players :( try again -> "))
    playerlist = range(0,player)
    return(playerlist)
    
#print(players())
#print(new_hand())
# this function handles adding cards
def addcards():
    pl = 1
    for ind, i in enumerate(player_hands):
        newdeck=[]
        bust = False
        # used to print string value of current player's deck
        for x in i:
            newdeck.append(str(x))
        # user input to determine if card is addded
        plyr_hit = input('player '+str(pl)+' your deck: '+str(newdeck) +' do you want to hit? y/n ->')
        plyr_hit = plyr_hit.lower()
        # checks input
        while plyr_hit == 'y' or plyr_hit == 'yes':
            player_hands[ind] = player_hands[ind] + [deck.deck[0]]
            # deletes first item in the deck once it has been added to a player's deck
            del(deck.deck[0])
            total = []
            for x in player_hands[ind]:
                total.append(x.ctype)
            vals = []
            for n in total:
                # will append the integer value of each card in player's deck
                vals.append(values[n])
            # if sum of all cards in player's deck > 21 bust and prevent player from hitting again
            if sum(vals) > 21:
                bust = True
                plyr_hit = 'n'
            newdeck = []
            #print(vals)
            #print(total)
            for x in player_hands[ind]:
                    newdeck.append(str(x))
            # prompts player to hit if player's deck < 21
            if bust == False:
                plyr_hit = input('your deck: '+str(newdeck)+\
                    ' would you like to hit again? ' )
            else:
                input('your deck: '+str(newdeck)+', You have busted press any key to continue')
        clear_screen()
        pl = pl+1
        input('press ENTER to continue')
        clear_screen()
# determines winner/winners of the game
def winner():
    # builds list of all player deck sums 
    for n, i in enumerate(player_hands):
        for num, x in enumerate(i): 
            i[num] = values[x.ctype]
        # objects in player hands are replaced with their integer sum values 
        player_hands[n] = sum(i)
    print(player_hands)
    # vars for win status
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
# promts user to play again
def play_again():
    global gamestatus
    placeholder = input('would you like to play again? y/n -> ')
    if placeholder == 'y' or placeholder == 'yes':
        gamestatus = True
    else: 
        gamestatus = False
# starts the game
def start():
    input("Blackish Jack - by:Faris Hijazi, Noah Boihem ----- "+\
                " press ENTER to continue")
    # only runs while gamestatus true
    while(gamestatus == True):
        # main loop
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

















