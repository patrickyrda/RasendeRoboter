from game.robot import Robot
from game.board import Board, obstacles

board = Board()

def test_robot_move_right():
    print(obstacles["Middle_Barrier"])
    print("\nHELLO")
    board.board[0][7].val = 164
    print("\n")
    robot = Robot(1, 0, 7)
    board.print_board()
    print("\n")
    x, y = robot.move_right(board.board)
    print(x)
    print(" ")
    print(y)

def test_robot_move_left():
    board.board[0][7].val = 164
    print("\n")
    robot = Robot(1, 0, 7)
    board.print_board()
    print("\n")
    x, y = robot.move_left(board.board)
    print(x)
    print(" ")
    print(y)

def test_robot_move_down():
    board.board[0][7].val = 164
    print("\n")
    robot = Robot(1, 0, 7)
    board.print_board()
    print("\n")
    x, y = robot.move_down(board.board)
    print(x)
    print(" ")
    print(y)

def test_robot_move_up():
    board.board[15][12].val = 164
    print("\n")
    robot = Robot(1, 15, 12)
    board.print_board()
    print("\n")
    x, y = robot.move_up(board.board)
    print(x)
    print(" ")
    print(y)