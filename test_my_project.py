import random
suits = ['♠', '♣', '♦', '♥']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = {rank + suit: [ranks.index(rank) + 6, suit] for rank in ranks for suit in suits}

list_deck = list(deck)

def trump():
    pass

def hand(deck: dict):
    hand = random.sample(list(deck.keys(), 6))

    return hand
print(list_deck)