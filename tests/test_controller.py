from game.controller import Controller
from game.interface import RobotGame
import tkinter as tk
def test_start():
    root = tk.Tk()
    gui = RobotGame(root, "facile")
    controller = Controller(gui)
    controller.initialize_game()
    

