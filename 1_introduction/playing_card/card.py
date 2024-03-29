suit_list_string = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

rank_list_dict = {
    'Ace' : { 'ace_low' : 1, 'ace_high' : 11 }, 
    'Two' : 2, 
    'Three': 3, 
    'Four' : 4, 
    'Five' : 5, 
    'Six'  : 6, 
    'Seven' : 7, 
    'Eight' : 8, 
    'Nine' : 9, 
    'Ten' : 10, 
    'Jack' : 10, 
    'Queen' : 10, 
    'King' : 10
}

rank_list_string = list(rank_list_dict.keys())
print(rank_list_string)
#Perhaps use inheritance for card games? 
class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self.suit_list = suit_list_string
        self.rank_list = rank_list_string

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

    def card_power(self):
        
    
        return rank_list_dict[self.rank]