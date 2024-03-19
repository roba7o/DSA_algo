from card import Card
from participant import Participant
import random

suit_list = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
rank_list = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

class Game:
    def __init__(self, game):
        self.game = None
        
        self.deck = []

    def establish_linear_deck(self):
        suit_list = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        rank_list = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        for suit in suit_list:
            for rank in rank_list:
                self.deck.append(Card(suit, rank))

    def print_list_of_deck_objects(self):
        for card in self.deck:
            print(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def __str__(self):
        return f"playing {self.game}"
    

class BlackJack(Game):
    def __init__(self, game):
        super().__init__(game)


    
def main():
    poker_game = Game("Poker")

    #Standard Deck
    poker_game.establish_linear_deck()
    poker_game.print_list_of_deck_objects()
    print(f"there is {len(poker_game.deck)} cards in this unshuffled deck")

    print("_______________________________")

    #Shuffled deck
    poker_game.shuffle_deck()
    poker_game.print_list_of_deck_objects()
    print(f"there is {len(poker_game.deck)} cards in this shuffled deck")

if __name__ == "__main__":
    main()
