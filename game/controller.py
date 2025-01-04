from algorithms import bfs, dls, As
from interface import RobotGame
class Controller:
    def __init__(self, gui):
        self.gameState = None
        self.difficulty = None
        self.gui = gui


    
    def initialize_game(self):
        self.gui.difficulty_window()
        print("\nDifcficulty is: ", self.difficulty)


    def easy_mode():
        # player will estimate the amount of moves and then move, Then ai will return a result, if no result then player wins, if result bigger than players result then player win
        # if not AI will show the result
        pass