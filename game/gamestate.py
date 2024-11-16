from board import Board
from robot import Robot

class GameState:

    def __init__(self, board : Board, robot1 : Robot, robot2 : Robot, robot3 : Robot, robot4 : Robot):
        self.board = board
        self.robot1 = robot1
        self.robot2 = robot2
        self.robot3 = robot3
        self.robot4 = robot4
        self.target = [0,0]
        self.robot_target = 0


    def define_target():
        # define the target of the round, it will return position to be reached as well as code of the robot to reach it, 
        # will have to handle association of the targets to the colors of the robots 
        pass
    def move_robot():
        # Move robot, handle all logic of barriers, where do they point
        pass    

    def is_target_reached():
        # Check if target has been reached by the right robot
        pass

    