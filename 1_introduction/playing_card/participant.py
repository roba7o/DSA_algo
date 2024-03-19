from game import Game

class Participant:
    def __init__(self, participant):
        self._participant = participant
        self.participant_list = ["player", "computer_player", "dealer"]
        self._hand = []

    @property
    def participant(self):
        return self._participant
    
    @participant.setter
    def participant(self, set_participant):
        if set_participant not in self.participant_list:
            raise ValueError("Not a valid participant")
        self._participant = set_participant

class Player(Participant):
    def __init__(self, participant, type_player):
        super().__init__(participant)
        self._bank = self.types_of_player[type_player]
        self._type_player = type_player
        self.types_of_player = {"high_roller": 1000000, "hobbiest": 100000, "casual" : 10000, "stag_do" : 1000}

    @property
    def type_player(self):
        return self._type_player
    
    @type_player.setter
    def type_player(self, set_type_player):
        if set_type_player not in self.types_of_player.keys:
            raise ValueError(f"Enter a valid type of player: {list(self.types_of_player.keys)}")
        self._type_player = set_type_player
            
        

class Dealer(Participant):
    def __init__(self, participant):
        super().__init__(participant)
        self.dealer_purse = 100000000   #setting the casino to 10 mil. Perhaps ban a player if hes close to earning too much.
        self.deck = Game.establish_linear_deck()
    

