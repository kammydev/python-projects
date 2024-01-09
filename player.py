import math 
import random

    # initialize the player class
class player:
    def __init__(self, letter):
        # Letter is X or O
        self.letter = letter

    def getMove(self , Game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, Game):
        square = random.choice(Game.availableMoves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def getMove(self, Game):
        validSquare = False
        val = None
        while not validSquare:
            square = input(self.letter + '\'s turn. Input move (0-9)')

            try:
                val = int(square)
                if val not in Game.availableMoves():
                    raise ValueError
                validSquare = True
            except ValueError:
                print("Invalid square. Try again.")

        return val
