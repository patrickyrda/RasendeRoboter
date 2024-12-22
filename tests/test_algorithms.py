from game.board import Board
from game.state import State
from game.robot import Robot
from algorithms.bfs import bfs

board = Board()
heuristics = board.heuristics_board(6,11)
# red = Robot(0, 0, 15)
red = Robot(0, 15, 13)
green = Robot(1, 5, 4)
blue = Robot(2, 7, 9)
yellow = Robot(3, 14, 10)

parent = State(board, red, green, blue, yellow, (5, 0), 0)
parent.check_setup()
def test_bfs():
    print("\nThis is the test bfs")
    result = bfs(parent)
    for noeud in result:
        print("\n")
        print(noeud.board.print_board())

    print(f"\nThe result has a size of : {len(result)}")