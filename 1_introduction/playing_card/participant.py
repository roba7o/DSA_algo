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
        self.stake = None

    def add_card(self, card):
        if isinstance(card, Card):
            self.hand.append(card)
        else:
            raise ValueError("Not a valid card")
        
    def remove_stake_from_budget(self, stake):
        self.budget -= stake

    #each computer participant should make a move same way. players will overide this fucntion for input 
        
    def make_move(self):
        if self.evaluate_deck < 17:
            return True
        return False

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

    def print_hand_list(self):
        return ", ".join(str(card) for card in self.hand)
    
    def evaluate_deck(self):
    #todo make this for computer
        non_ace_sum = 0
        num_of_aces = 0
        total_sum = 0
        for card in self.hand:
            if card.rank != "Ace":
                non_ace_sum += card.card_power()
            else:
                num_of_aces += 1
        if num_of_aces > 1:
            total_sum = non_ace_sum + num_of_aces
        else:
            if non_ace_sum < 11:
                total_sum += 11
            else:
                non_ace_sum += 1
        return total_sum
  

class MyPlayer(Participant):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def evaluate_deck(self):
        sum = 0
        for card in self.hand:
            if card.rank != "Ace":
                sum += card.card_power()
            else:
                while True:
                    try:
                        ace_decision = int(input("11 or 1 for Ace? "))
                        sum += ace_decision
                        break
                    except ValueError:
                        print("Please select 1 or 11")

    def make_move(self):
        while True:
            try:
                move = input("Hit or Stand")
                if move.lower().startswith("h"):
                    return True
                elif move.lower().startswith("s"):
                    return False
                else:
                    raise ValueError("hit or stand mate")
            except ValueError:
                print("please be normal")

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
    
    #todo make move for computer based on score. returns true or f
         

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.name = "dealer " + self.random_name
        self.budget = 10000000
    
    def __str__(self):
        return f"Hello i am {self.name}"

