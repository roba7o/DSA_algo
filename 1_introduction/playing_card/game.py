from card import *
import random
from participant import *



class Game:
    def __init__(self, game):
        self.game = None
        self.deck = [Card(suit, rank) for suit in suit_list_string for rank in rank_list_string]
        random.shuffle(self.deck)
        self.number_of_players = None
        self.participants = []
        self.dealer = None

    def print_list_of_deck_objects(self):
        for card in self.deck:
            print(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def __str__(self):
        return f"playing {self.game}"
    
    def get_number_of_players(self):
        while True:
            try:
                user_input = int(input("how many players (Max 4 at a table) "))
                if user_input not in range(4):
                    raise ValueError("Simple bro just pick a number")
                self.number_of_players = user_input
                break
            except ValueError:
                print("Enter a number freak")
    
    def establish_player_types(self):
        #dealer
        self.dealer = Dealer()
        print(self.dealer)

        #myself
        player_name = input("Whats your name? ")
        my_player = MyPlayer(player_name)
        print(my_player)
    
        my_player.choose_budget()
        self.participants.append(my_player)

        print(f"number of players is {self.number_of_players}")
        #computer players
        for _ in range(self.number_of_players):
            
            computer_player = ComputerPlayer()
            #print(computer_player)
            self.participants.append(computer_player)
        
    def debug_list_budgets(self):
        for player in self.participants:
            print(f"{player.name} has {player.budget}")


    def make_bet(self):
        for player in self.participants:
            player.place_bet()



# class BlackJack(Game):
#     def __init__(self, game, number_of_players):
#         super().__init__(game, number_of_players)
    
def main():
    poker_game = Game("Black Jack")


    #1) ask how many and what type of player is playing
    poker_game.get_number_of_players()
    poker_game.establish_player_types()

    poker_game.debug_list_budgets()
    poker_game.make_bet()


    #TO DO, at this point. Everyone should have their own name and budget and initial bet (parent class) 

    #2) Establish dealer deck and deal hand.

        #-> after this everyone should have their own 2 hands. and the screen should print:
            # the dealers (at first 1. face-up 2. hole-card)
            # every players cards face up (print hand function with dealers being diferent maybe if statement for the first round)


    #3) 2) ask player ask what bet they want with their hand (hit or stand)
        #for player in players - > player.make move
        #if computers players hand > 16 - stay
    
        #once all players either stand or bust then dealer rebeals hole card.
        #dealer must hit until above 17

        
    #5) #if hit blackjack -> 1.5 stake back unless dealer also blackjack then push: player gets stake back 
       
       #this doesnt need coded -> maybe prevent the player making hit in their make_move function as it should print (you have blackjack return 'stand' (so ask anyway but always result stand))


    #extra
    """
    Split: If a player's first two cards have the same value, they can choose to split the cards into 
            two separate hands and play each hand individually. 
            This requires an additional bet equal to the original bet.


    Double Down: - easy to code (ask user, and for computer if less than 12 then one in every 6)
    After receiving the first two cards, a player may 
                 choose to double their original bet and receive only one more card.
    """    




if __name__ == "__main__":
    main()
