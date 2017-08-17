from hand import Hand

class Player(object):
    def __init__(self, name, current_bet, current_pool=100):
        self.name = name
        self.current_pool = current_pool
        self.current_bet = current_bet
        self.current_hand = Hand()

    def bankrupt(self):
        return self.current_pool <= 0
