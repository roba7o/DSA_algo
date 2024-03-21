import json
import random
from card import *

class Participant:
    def __init__(self):
        self.hand = []
        self.person = self.generate_random_name_and_budget()
        #print(f"testing if i have a person: {self.person}")
        self.random_name, self.random_budget = list(self.person.items())[0]
        #print(f"testing if if i have name {self.random_name} and budget: {self.random_budget}")
        self.name = None
        self.budget = None

    def add_card(self, card):
        if isinstance(card, Card):
            self.hand.append(card)
        else:
            raise ValueError("Not a valid card")
        
    def remove_stake_from_budget(self, stake):
        self.budget -= stake

    #each participant should make a move same way.
    def make_move(self, move):
        while True:
            try:
                move = input("Hit or Stand")
                if move.lower().startswith("h"):
                    self.get_card()
                    break
                elif move.lower().startswith("l"):
                    break
                else:
                    raise ValueError("hit or stand mate")
            except ValueError:
                print("please be normal")

    def generate_random_name_and_budget(self):
        with open('names_with_numbers.json', 'r') as name_json_file:
            name_json = json.load(name_json_file)
            return random.choice(name_json)
            # print(self.person)
            # print(type(self.person))

    def assign_random_name(self):
        self.name = self.random_name
    
    def assign_random_budget(self):
        self.budget = self.random_budget

    def print_name(self):
        print(self.name)
  

class MyPlayer(Participant):
    def __init__(self, name):
        super().__init__()
        self.name = name

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
                    raise ValueError("Please choose another casino mr gates")
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
                input_bet = int(input(f"How much you betting mate? You have {self.budget}"))
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
         

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.name = self.random_name
        self.budget = 10000000
    
    def __str__(self):
        return f"Hello my name is {self.name} and I am your dealer"

