import math
import random


class Player:
    # letter is x or o
    def __init__(self, letter):
        self.letter = letter

    # we need all players to get the next move given a game
    def get_move(self, game):
        return random.choice(game.available_moves())


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid square to get a next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn.Input move (0-8)")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if user enters valid empty box number
            except ValueError:
                print("Invalid square. Try again")

        return val
