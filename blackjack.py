import random

class Deck:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

class Player:
    def __init__(self):
        self.hand = []

def deal(deck,players):
    while len(players[len(players) - 1].hand) < 2:
        for player in players:
            player.hand.append(deck.cards.pop(0))

def hit(deck,player):
    player.hand.append(deck.cards.pop(0))

def shuffle(deck):
    while len(deck.cards) < 52:
        deck.cards.extend(deck.cards.copy())
    random.shuffle(deck.cards)