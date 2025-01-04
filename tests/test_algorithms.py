from game.board import Board
from game.state import State
from game.robot import Robot
from algorithms.bfs import bfs
from algorithms.As import As
from algorithms.dls import dls



board = Board()
# heuristics = board.heuristics_board(6,11)
# red = Robot(0, 15, 15)
red = Robot(0, 0, 12)
# red = Robot(0, 9, 8)
# red = Robot(0, 15, 13)
green = Robot(1, 5, 4)
blue = Robot(2, 7, 9)
yellow = Robot(3, 14, 10)
# Color red for robot target
parent = State(board, red, green, blue, yellow, (5, 0), 3)
parent.check_setup()
def test_bfs():
    print("\nThis is the test bfs")
    result = bfs(parent)
    # Have to add control here when return is none
    for noeud in result:
        print("\n")
        print(noeud.board.print_board())
        print("\n")
        noeud.board.heur(noeud.board.heuristics_board_new(5,0))

    print(f"\nThe result has a size of : {len(result)}")



def test_as():
    print("\nThis is the test as")
    result = As(parent)
    if result is None:
        print("\nNo Result")
    else:
        for noeud in result:
            print("\n")
            print(noeud.board.print_board())

    print(f"\nThe result has a size of : {len(result)}")

def test_dls():
    visited = set()
    result = dls(parent, visited)
    for noeud in result:
        print("\n")
        print(noeud.board.print_board())

    print(f"\nThe result has a size of : {len(result)}")

def test_euristics():
    print("\n")
    parent.board.print_board()
    print("\n")
    print(parent.board.heuristics_board_new(5,0))
    print("\nNow the old one")
    print(parent.board.heuristics_board(5,0))
