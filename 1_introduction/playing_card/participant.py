import json
import random

types_of_player = {"high_roller": 1000000, "hobbiest": 100000, "casual" : 10000, "stag_do" : 1000}

class Participant:
    def __init__(self):
        self.hand = []
        self.person = self.generate_random_name_and_budget()
        #print(f"testing if i have a person: {self.person}")
        self.random_name, self.random_budget = list(self.person.items())[0]
        #print(f"testing if if i have name {self.random_name} and budget: {self.random_budget}")
        self.name = None

    

    #each participant should make a move same way.
    def make_move(self, game, move):
        while True:
            try:
                move = input("Hit or Stand")
                if move.lower() == "hit":
                    self.get_card()
                    break
                elif move.lower() == 'stand':
                    break
                else:
                    raise ValueError("hit or stand mate")
            except ValueError:
                print("please be normal")

    def get_card(self, game):
        self.hand.append(game.take_card())

    def generate_random_name_and_budget(self):
        with open('names_with_numbers.json', 'r') as name_json_file:
            name_json = json.load(name_json_file)
            return random.choice(name_json)
            # print(self.person)
            # print(type(self.person))

    def assign_random_name(self):
        self.name = self.random_name

    def print_name(self):
        print(self.name)
  

class MyPlayer(Participant):
    def __init__(self, name):
        self.name = name
        self.budget = None

    def __str__(self):
        return f"Hello my name is {self.name}"

    def choose_budget(self):
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
        while True:
            try:
                
            except ValueError:
                print("A NORMAL BET PLEASE")



class ComputerPlayer(Participant):
    def __init__(self):
        super().__init__()
        self.name = "Random player " + self.random_name
        self.budget = self.random_budget


    def __str__(self):
        return f"Hello my name is {self.name}"
    

        

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.name = self.random_name
        self.budget = 10000000
    
    def __str__(self):
        return f"Hello my name is {self.name} and I am your dealer"

