import random
from re import S
from turtle import Turtle

suits = ('Copas','Ouros','Espadas','Paus')
ranks = ('Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Valete','Rainha','Rei','As')
values = {'Dois':2,'Três':3,'Quatro':4,'Cinco':5,'Seis':6,'Sete':7,'Oito':8,'Nove':9,'Dez':10,'Valete':11,'Rainha':12,'Rei':13,'As':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " de " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #Create the Card Object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self,name):
        
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            #List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            #For a single card object
            self.all_cards.append(new_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def __str__(self):
        return f'Jogador {self.name} tem {len(self.all_cards)} cartas'

#GAME SETUP
player_one = Player("Um")
player_two = Player("Dois")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player_one.all_cards) == 0:
        print('Jogador 1, sem cartas! Jogador 2 ganhou!')
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print('Jogador 2, sem cartas! Jogador 1 ganhou!')
        game_on = False
        break

    #START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    

    #While at_war

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print('GUERRA!')

            if len(player_one.all_cards) < 3:
                print("Jogador 1 não é capaz de declara Guerra")
                print("Jogador 2 ganhou!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 3:
                print("Jogador 2 não é capaz de declara Guerra")
                print("Jogador 1 ganhou!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

    player_one.shuffle()
    player_two.shuffle()