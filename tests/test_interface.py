from algorithms.bfs import bfs
from game.interface import RobotGame
from game.list_interface import StateDisplayer
import tkinter as tk
def test_gui_launch():
    from game.interface import main
    try:
        main()  # Vérifie que l'interface peut se lancer
        assert True
    except Exception as e:
        assert False, f"L'interface a échoué à se lancer : {e}"


from game.board import Board
from game.state import State
from game.robot import Robot
from algorithms.bfs import bfs
from algorithms.As import As
from algorithms.dls import dls



board = Board()
# heuristics = board.heuristics_board(6,11)
# red = Robot(0, 15, 15)
red = Robot(0, "red", 0, 12)
# red = Robot(0, 9, 8)
# red = Robot(0, 15, 13)
green = Robot(1, "green", 5, 4)
blue = Robot(2, "blue", 7, 9)
yellow = Robot(3, "yellow", 14, 10)
# Color red for robot target
parent = State(board, red, green, blue, yellow, (5, 0), 3)
parent.check_setup()
'''
def test_list_display():
    robot_game = RobotGame(parent)
    result_list = bfs(parent)
    robot_game.set_result_state_list(result_list)
    print("\nBFS FINISHED")
    robot_game.display_list()
    '''

def test_list_display():
    result_list = bfs(parent)
    print("\nBFS FINISHED")
    print("size of the result is : ",len(result_list))
    root = tk.Tk()
    displayer = StateDisplayer(root, result_list)
    displayer.run()