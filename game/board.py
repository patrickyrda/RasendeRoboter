from boardpiece import BoardPiece
from robot import Robot
import numpy as np
'''
Green robot = 1
Red robot = 2
Blue robot = 3
Yellow robot = 4
Top barrier = 5
Down barrier = 6
Left barrier = 7
Right barrier = 8
Colored barrier = 9
Blocked center = 10 
add numbers for the 17 targets 
'''
class Board:
    def __init__(self):

        self.board = np.zeros((16, 16), dtype=int)
        self.piece1 = BoardPiece().set_obstacles()
        self.piece2 = BoardPiece().set_obstacles()
        self.piece3 = BoardPiece().set_obstacles()
        self.piece4 = BoardPiece().set_obstacles()
        self.robots_initial_pos = np.zeros((4, 2), dtype=int)
        self.target = [0,0]
    def place_robot_random(robot: Robot):
        # place robot in random position
        pass
    def assemble_pieces():
        # assemble boardpieces
        pass

    def place_targets():
        # place targets in random positions of the board once it has been assembled
        pass

    def place_obstacles():
        # place obstacles in random positions, consider probabilities, walls and colored barriers AS WELL AS THE BLOCKED 4 SQUARES OF THE CENTER
        pass




