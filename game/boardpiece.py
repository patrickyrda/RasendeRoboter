from robot import Robot
import numpy as np

class BoardPiece:
    def __init__(self):
        self.size = 8
        self.boardpiece = np.zeros((self.size, self.size), dtype=int)
