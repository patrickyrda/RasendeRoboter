from algorithms.helpers import get_next_states, is_goal
from game.board import Board
from game.state import State
from game.robot import Robot

board = Board()
heuristics = board.heuristics_board(6,11)
red = Robot(1, 0, 0)
green = Robot(1, 5, 4)
blue = Robot(2, 7, 9)
yellow = Robot(3, 14, 10)

parent = State(board, red, green, blue, yellow, (6, 11), 1)
parent.check_setup()
'''
def test_get_next_states():
    result = get_next_states(parent, heuristics)
    print("\n")
    for desc, res in result:
        board.print_board()
        print(desc)
        print("\n")
        print(res.board.print_board())

    print("\n")
    print(heuristics)

def test_is_goal():

    state = State(board, red, green, blue, yellow, (5, 0), 0)
    print("\n first ")
    print(is_goal(state))
    state.slide_robot_down(state.robots[0])
    print("\n second ")
    print(is_goal(state))
    print("\Specs: \n")
    print(state.board.board[state.target[0]][state.target[1]].has_robot)
    print(" ")
    print(state.board.board[state.target[0]][state.target[1]].has_target)
    print(" ")
    print(state.board.board[state.target[0]][state.target[1]].val)
'''