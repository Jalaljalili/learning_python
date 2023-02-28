class Card:
    symbols = { 'S' : {'name': 'Spade',   'unicode': '\u2660'},
                'H' : {'name': 'Heart',   'unicode': '\u2665'},
                'D' : {'name': 'Diamond', 'unicode': '\u2666'},
                'C' : {'name': 'Club',    'unicode': '\u2663'}}
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def __format__(self, formatstr):
        out = self.rank + self.symbols[self.suit]['unicode']
        return '{0:{spec}}'.format(out, spec=formatstr)
    
    def __str__(self):
        return self.rank + ' of ' + self.symbols[self.suit]['name']
    
    def __repr__(self):
        return self.__class__.__name__ + '(\'' + self.rank + '\', \'' + self.suit + '\')'
    
deck = [Card(rank, suit)
        for rank in ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        for suit in 'SHDC' ]

from random import choice

c1 = choice(deck) 

print('Your random card is {}'.format(c1))       
print('Your random card is {card!s}'.format(card=c1))
print('Your random card is {card!r}'.format(card=c1))