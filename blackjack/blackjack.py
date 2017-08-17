from game import Game
from player import Player

if __name__ == '__main__':
    username = raw_input("What is your name?\n")
    player = Player(username, 20)
    game = Game(player)
    bet = ""
    while not player.bankrupt() and not bet == "exit":
        try:
            bet = float(raw_input("What would you like to bet? You currently have " + str(player.current_pool) + "\n"))
        except:
            print("Yo, put some positive number")
            break

        if bet <= 0:
            print("Yo, put some positive number")
        elif bet > player.current_pool:
            print("Cannot bet more than you have, which is " + str(player.current_pool))
        else:
            player.current_bet = float(bet)
            print("Hi " + player.name + ". You are betting " + str(player.current_bet) + " dollars.")
            game.run()
    print("You are done")
