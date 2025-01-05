from game.controller import Controller
from game.robot import Robot
from game.state import State
from game.board import Board


def main():
    board = Board()
    red = Robot(0, "red", 15, 15)
    green = Robot(1, "green", 5, 4)
    blue = Robot(2, "blue", 7, 9)
    yellow = Robot(3, "yellow", 14, 10)
    state = State(board, red, green, blue, yellow, (5, 0), 0)
    state.change_state()
    controller = Controller(state)
    controller.play()






if __name__ == "__main__": 
    main()