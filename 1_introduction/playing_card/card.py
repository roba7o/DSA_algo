import random

#Perhaps use inheritance for card games? 


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self.suit_list = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.rank_list = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, new_suit):
        if new_suit not in self.suit_list:
            raise ValueError("Invalid suit")
        self._suit = new_suit

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, new_rank):
        if new_rank not in self.rank_list:
            raise ValueError("Invalid Rank")
        self._rank = new_rank



