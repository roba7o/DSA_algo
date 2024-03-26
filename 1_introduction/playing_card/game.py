from card import *
import random
from participant import *

#TODO fix * import

class Game:
    def __init__(self, game):
        self.game = game
        self.deck = [Card(suit, rank) for suit in suit_list_string for rank in rank_list_string]
        random.shuffle(self.deck)
        self.number_of_players = None
        self.participants = []
        self.dealer = None

    #! for debugging
    def print_list_of_deck_objects(self):
        for card in self.deck:
            print(card)

    def debug_list_budgets(self):
        for player in self.participants:
            print(f"{player.name} has {player.budget}")

    def print_part_stand_scores(self):
        for player in self.participants:
            print(f"{player.name} has {player.stand_score}")
    #! for debugging


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
    
    def establish_participant_types(self):
        """
        Creates list of participants who will make moves
        """
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
            self.participants.append(computer_player)
        
    

    def remove_card_from_deck(self, person):
        """
        takes once card from deck and adds to person
        """
        card_to_remove = self.deck[0]
        person.add_card(card_to_remove)
        self.deck.remove(card_to_remove)

    
    def establish_stake(self):
        """
        establishes stake for each player. 
        TODO can probably go into another function as it only happens once in init
        """
        for player in self.participants:
            bet = player.place_bet()
            player.remove_stake_from_budget(bet)
            player.stake = bet           

    
    def establish_initial_hand(self):
        """
        gives each partipant 2 cards
        """
        self.remove_card_from_deck(self.dealer)
        self.remove_card_from_deck(self.dealer)

        for player in self.participants:
            self.remove_card_from_deck(player)
            self.remove_card_from_deck(player)

    def print_hands(self, round_hidden):
        """
        prints hand.
        """
        if round_hidden is True:
            print("INITIAL HANDS!")
            print(f"{self.dealer.name} has {self.dealer.hand[0]} and mystery")
            for player in self.participants:
                print(f"{player.name} has {player.print_hand_list()}")
            print("**************************************")
        else:
            print("PLAYERS HAVE STAKED HANDS!")
            print(f"{self.dealer.name} has {self.dealer.print_hand_list()}")
            for player in self.participants:
                print(f"{player.name} has {player.print_hand_list()}")
            print("**************************************")
    
    def print_participants(self):
        remaining_players = [player.name for player in self.participants]
        return ", ".join(remaining_players)


    def dealer_makes_move(self):
        while True:
            self.dealer.stand_score = self.dealer.evaluate_deck()
            print(f"{self.dealer.name} you are on {self.dealer.stand_score}")
            move = self.dealer.make_move()
            if move:
                print(f"{self.dealer.name} HIT!")
                self.remove_card_from_deck(self.dealer)
                self.dealer.stand_score = self.dealer.evaluate_deck()
                print(f"{self.dealer.name} has {self.dealer.print_hand_list()} at score {self.dealer.stand_score}")
                
                if self.dealer.stand_score > 21:
                    print(f"{self.dealer.name} went BUST LMFAO at {self.dealer.stand_score}")
                    break
            else:
                print(f"{self.dealer.name} stands lol")
                print(f"{self.dealer.name} has {self.dealer.print_hand_list()} at {self.dealer.stand_score}")
                break


    #! TO DO GOT TO HERE
    def participants_make_move(self):
        for participant in self.participants:
            while True:
                participant.stand_score = participant.evaluate_deck()
                print(f"{participant.name} you are on {participant.stand_score}")
                move = participant.make_move()
                if move:
                    print(f"{participant.name} HIT!")
                    self.remove_card_from_deck(participant)
                    participant.stand_score = participant.evaluate_deck()
                    print(f"{participant.name} has {participant.print_hand_list()} at score {participant.stand_score}")
                    
                    if participant.stand_score > 21:
                        print(f"{participant.name} went BUST LMFAO at {participant.stand_score}... see ya!")
                        self.participants.remove(participant)
                        print(self.print_participants())
                        break
                else:
                    print(f"{participant.name} stands lol")
                    participant.stand_score = participant.evaluate_deck()
                    print(f"{participant.name} has {participant.print_hand_list()} at {participant.stand_score}")
                    break

    def establish_winnings(self):

        if self.dealer.stand_score > 21:
            print("Congrats all remaining players")
            for player in self.participants:
                print(f"nice play.. you won {player.stake}")
                player.budget += player.stake * 2
                player.stake = 0



        print("***********************************************")
        print("Remaining players... lets go!")       
        print("***********************************************")
        self.dealer.stand_score = self.dealer.evaluate_deck()
        
        print(f"{self.dealer.name} has {self.dealer.print_hand_list()} at {self.dealer.stand_score}")
        print("***********************************************")
        print("And for the players!")
        self.print_part_stand_scores()

        for player in self.participants:
            print()
            print(f"{player.name} has {player.print_hand_list()} at {player.stand_score}")
            if player.stand_score == 21 and len(player.hand) == 2:  
                print("You have BlackJack... nice one!")
                if self.dealer.stand_score == 21 and len(self.dealer.hand) == 2:
                    print(f"... but so did the dealer. Unlucky. Keep your stake of {player.stake}")
                    player.budget += player.stake
                    player.stake = 0
                else:
                    print(f"and the dealer didnt... you the winner. you won {player.stake}")
                    player.budget += player.stake * 2
                    player.stake = 0

            elif player.stand_score > 21:
                print(f"how tf did you make it this far. {player.name} you have lost already")
                self.participants.remove(player)
                break

            elif player.stand_score > self.dealer.stand_score:
                print(f"nice play.. you won {player.stake}")
                player.budget += player.stake * 2
                player.stake = 0

            elif player.stand_score < self.dealer.stand_score:
                print(f"unlucky mate you lost {player.stake}")
                player.budget -= player.stake
                player.stake = 0
            else:
                print(f"PUSH you have {player.stand_score} but so did the dealer")
                player.budget += player.stake
                player.stake = 0           
            print("/")

    
def main():
    game_on = True    
    while game_on:
        poker_game = Game("Black Jack")
        print(poker_game)

        #1) ask how many and what type of player is playing
        poker_game.get_number_of_players()
        poker_game.establish_participant_types()

        poker_game.debug_list_budgets()
        poker_game.establish_stake()

        #2) Establish dealer deck and deal hand.
        round_one = True
        poker_game.establish_initial_hand()  #all players get 3 cards, make the print function 
        poker_game.print_hands(round_one)
        round_one = False

        poker_game.participants_make_move()
        poker_game.print_hands(round_one)


        poker_game.dealer_makes_move()

        poker_game.establish_winnings()

        #todo refactor this repeated user input code to 
        while True:
            try:
                another_game = input("Another game? Yes/No: ")
                if another_game.lower().startswith('y'):
                    print("Allez")
                    break
                elif another_game.lower().startswith('n'):
                    print("Have a good day mate!")
                    game_on = False
                    break
                else:
                    print("yes or no mate")
            except ValueError:
                print("Enter a YES OR NO freak")

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
