import random
import pygame

suits = ['♠', '♣', '♦', '♥']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = {rank + suit: [ranks.index(rank) + 6, suit] for rank in ranks for suit in suits}
list_deck = list(deck)


def trump(suits: list):
    suit = random.sample(suits)
    return suit

    
def hand(deck: list):
    random_elements = random.sample(range(len(deck)), 6)
    hand = [deck[index] for index in random_elements]
    # deck = [element for index, element in enumerate(deck) if index not in hand] 
    return hand

def heap(hand: list):
    pass

def table(hand1: list, hand2: list):
    table = []
    
    return table


print(list_deck)