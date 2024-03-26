import json
import random
from card import *


class Participant:
    def __init__(self):
        self.hand = []
        self.stand_score = None
        self.random_person = self.generate_random_name_and_budget()
        self.random_name, self.random_budget = list(self.random_person.items())[0]
        self.name = None
        self.budget = None
        self.stake = None

    def generate_random_name_and_budget(self):
        with open('/Users/robertmatthew/Documents/programmingSelfStudy/DSA_algo/1_introduction/playing_card/names_with_numbers.json', 'r') as person_json_file:
            person_json = json.load(person_json_file)
            return random.choice(person_json)

    def assign_random_name(self):
        self.name = self.random_name
    
    def assign_random_budget(self):
        self.budget = self.random_budget

    def print_name(self):
        print(self.name)

    def print_hand_list(self):
        return ", ".join(str(card) for card in self.hand)
        
    def add_card(self, card):
        """
        adds card to players hand
        """
        if isinstance(card, Card):
            self.hand.append(card)
        else:
            raise ValueError("Not a valid card")
        
    def remove_stake_from_budget(self, stake):
        """
        removes stake from player
        """
        self.budget -= stake
        
    def make_move(self):
        """
        FOR COMPUTER returns boolean to take card or not. my_player will overwrite this 
        """
        if self.evaluate_deck() < 17:
            return True 
        return False

        
    """
    Evalaute deck
    1) add normal cards = normal-total
    2) count ace cards = ace_count
    3) use a function that chooses optimal ace combination with 21
    """

    def evaluate_deck(self):
        non_ace_total = 0
        num_of_aces = 0
        for card in self.hand:
            if card.rank != "Ace":
                non_ace_total += card.card_power()
            else:
                num_of_aces += 1
        total = non_ace_total

        for i in range(num_of_aces):
            #(num_of_aces - i - 1) is number of remaining aces (aka since Ace = 1 here its accounting for minumum extra total)
            #1 represents the 11, num_of_aces - i is the aces already accounted for in the loop
            if total + 11 + (num_of_aces - i - 1) <= 21:
                total += 11
            else:
                total += 1
        return total

class MyPlayer(Participant):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def evaluate_deck(self):
        total = 0
        for card in self.hand:
            if card.rank != "Ace":
                total += card.card_power()
            else:
                while True:
                    try:
                        if total + 11 > 21:
                            print("Adding 11 here busts so ace is 1")
                            total + 1
                        else:
                            ace_decision = int(input("11 or 1 for Ace? "))
                            total += ace_decision
                            break
                    except ValueError:
                        print("Please select 1 or 11")
        return total

    def make_move(self):
        while True:
            move = input("Hit or Stand: ").lower()
            if move.startswith("h"):
                return True
            elif move.startswith("s"):
                return False
            else:
                print("Please enter 'hit' or 'stand'.")

    def __str__(self):
        return f"Hello my name is {self.name}"

    def choose_budget(self):
        """
        Assigns self.budget
        """
        while True:
            try:
                user_input = int(input("Whats your budget for this table (1000-100000)? "))
                if user_input < 1000:
                    raise ValueError("Too low for this table")
                if user_input > 100000:
                    raise ValueError("Please choose another casino mr wayne")
                self.budget = user_input
                break
            except ValueError:
                print("Enter a number freak")

    def place_bet(self):
        """
        returns bet
        """
        while True:
            try:
                input_bet = int(input(f"How much you betting mate? You have {self.budget}: "))
                if input_bet > self.budget:
                    raise ValueError("Dude you dont have that kind of money, allez!")
                elif input_bet > 0.9 * self.budget:     
                    while True:
                        try:
                            are_you_sure = input("Are you sure you want to bet that much? Y/N")
                            if are_you_sure.lower().startswith('y'):
                                return input_bet
                            elif are_you_sure.lower().startswith('n'):
                                break
                            else: 
                                raise ValueError("Please enter 'Y' or 'N'.")
                        except ValueError as e:
                            print(e)
                return input_bet
            except ValueError as e:
                print(e)

class ComputerPlayer(Participant):
    def __init__(self):
        super().__init__()
        self.name = "Random player " + self.random_name
        self.budget = self.random_budget

    def __str__(self):
        return f"Hello my name is {self.name}"
    
    def place_bet(self):
        return random.randint(1000, self.budget)
    
    #todo make move for computer based on score. returns true or f

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.name = "dealer " + self.random_name
        self.budget = 10000000
    
    def __str__(self):
        return f"Hello i am {self.name}"

