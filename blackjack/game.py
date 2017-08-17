
from dealer import Dealer
from player import Player
from deck import Deck
from hand import Hand

class Game(object):
    def __init__(self, player):
        self.player = player
        self.dealer = Dealer()
        self.deck = Deck()
        self.game_over = 0 # 0: false, 1: player stay, 2: blackjack or bust

    def start(self):
        self.player.current_hand = Hand()
        self.dealer = Dealer()
        self.deck = Deck()
        self.game_over = 0
        self.deck.shuffle()

    def deal(self, num_card, player):
        for _ in xrange(num_card):
            player.current_hand.add_card(self.deck.draw_card())

    def run(self):
        self.start()
        # deal to player
        self.deal(2, self.player)
        # dealer to dealer
        self.deal(2, self.dealer)
        # show player hand
        print "Player: " + self.player.current_hand.show()

        player_hand = self.player.current_hand
        dealer_hand = self.dealer.current_hand

        # # show dealer hand
        print "Dealer: " + dealer_hand.show(hide_dealer=True)

        if player_hand.is_blackjack() or dealer_hand.is_blackjack():
            self.game_over = 2

        while not self.game_over:
            user_choice = int(raw_input("1: Hit, 2: Stay\n"))
            if int(user_choice) == 1:
                self.deal(1, self.player)
                print "Player: " + player_hand.show()
                print "Dealer: " + dealer_hand.show(hide_dealer=True)
                if player_hand.is_bust():
                    self.game_over = 2
            else:
                self.game_over = 1


        if self.game_over == 1:
            print dealer_hand.show(hide_dealer=True)
            while max(dealer_hand.calculate()) < 17:
                self.deal(1, self.dealer)
                print dealer_hand.show()

        print("Final Hands")
        print "Player: " + player_hand.show()
        print "Dealer: " + dealer_hand.show()
        print "-----"

        if self.determine_result() == 0:
            print("Too bad. You lose.")
            self.player.current_pool -= self.player.current_bet
            print("You have " + str(self.player.current_pool) + " dollars.")
        elif self.determine_result() == 1:
            print("Tied game!")
            print("You have " + str(self.player.current_pool) + " dollars.")
        else:
            print("Awesome. You win.")
            self.player.current_pool += self.player.current_bet * 1.5 if player_hand.is_blackjack() else self.player.current_bet
            print("You have " + str(self.player.current_pool) + " dollars.")

    def determine_result(self):
        if self.player.current_hand.is_bust():
            return 0

        if self.player.current_hand.is_blackjack():
            if self.dealer.current_hand.is_blackjack():
                return 1
            return 2

        if self.dealer.current_hand.is_blackjack():
            return 0
        if self.dealer.current_hand.is_bust():
            return 2

        if self.player.current_hand < self.dealer.current_hand:
            return 0
        elif self.player.current_hand == self.dealer.current_hand:
            return 1
        else:
            return 2

    def end(self):
        self.players = []
        self.dealer = None
        self.deck = None
