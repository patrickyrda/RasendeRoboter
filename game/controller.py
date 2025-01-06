from algorithms.bfs import bfs
from algorithms.dls import dls
from algorithms.asalgo import As_intorlist
from .new_interface import DifficultySelector
from .board import Board
from .robot import Robot
from .state import State
from .interface import RobotGame
from .list_interface import StateDisplayer
import tkinter as tk
from copy import deepcopy
from tkinter import messagebox
import os
class Controller:
    def __init__(self, state):
        
        self.gameState = state
        self.gameState.check_setup()
        self.difficulty = None
        self.robotGame = RobotGame(deepcopy(self.gameState))
    
    def show_message(self, message):
        messagebox.showinfo("Game Message", message)
    
    
    def play(self):
        
        dfsel = DifficultySelector(self)
        dfsel.display_difficulties()
        self.show_message(f"\nDifficulty selected: {self.difficulty}")

        if (self.difficulty == "Facile"):
            self.easy_mode()
        elif (self.difficulty == "Moyen"):
            self.medium_mode()
        elif (self.difficulty == "Difficile"):
            self.hard_mode()
        else:
            print("\nError")
    # -1 to exclude from the size the first state!
    def easy_mode(self):
        self.robotGame.display()

        result_list = dls(self.gameState)
        if (result_list is None and self.robotGame.has_won == False):
            self.show_message("\nYou lost and the AI too!")
            os.system('python main.py')
            return
        elif (result_list is None and self.robotGame.has_won == True):
            self.show_message("\nYou won against the AI that couldn't find an answer!!")
            os.system('python main.py')
            return

        if (self.robotGame.has_won == False or len(result_list) - 1 < self.robotGame.move_counter):
            self.show_message("\nYou lost against the AI!")
        elif(len(result_list) - 1 == self.robotGame.move_counter):
            self.show_message("\nIt's a tie!")
        elif(len(result_list) - 1 > self.robotGame.move_counter):
            self.show_message("\nYou won against the AI!")

        root = tk.Tk()
        statedisplay = StateDisplayer(root, result_list)
        statedisplay.run()


    def medium_mode(self):
        self.robotGame.display()

        result_list = As_intorlist(self.gameState)
        if isinstance(result_list, int):
            depth = result_list + 2
            result_list = dls(self.gameState, max_depth=depth)
        
        if (result_list is None and self.robotGame.has_won == False):
            self.show_message("\nYou lost and the AI too!")
            os.system('python main.py')
            return
        elif (result_list is None and self.robotGame.has_won == True):
            self.show_message("\nYou won against the AI that couldn't find an answer!!")
            os.system('python main.py')
            return
    
        if (self.robotGame.has_won == False or len(result_list) - 1 < self.robotGame.move_counter):
            self.show_message("\nYou lost against the AI!")
        elif(len(result_list) - 1 == self.robotGame.move_counter):
            self.show_message("\nIt's a tie!")
        elif(len(result_list) - 1 > self.robotGame.move_counter):
            self.show_message("\nYou won against the AI!")

        root = tk.Tk()
        statedisplay = StateDisplayer(root, result_list)
        statedisplay.run()

        

    def hard_mode(self):
        self.robotGame.display()

        result_list = bfs(self.gameState)
        if (result_list is None and self.robotGame.has_won == False):
            self.show_message("\nYou lost and the AI too!")
            os.system('python main.py')
            return
        elif (result_list is None and self.robotGame.has_won == True):
            self.show_message("\nYou won against the AI that couldn't find an answer!!")
            os.system('python main.py')
            return

        if (self.robotGame.has_won == False or len(result_list) - 1 < self.robotGame.move_counter):
            self.show_message("\nYou lost against the AI!")
        elif(len(result_list) - 1 == self.robotGame.move_counter):
            self.show_message("\nIt's a tie!")
        elif(len(result_list) - 1 > self.robotGame.move_counter):
            self.show_message("\nYou won against the AI!")

        root = tk.Tk()
        statedisplay = StateDisplayer(root, result_list)
        statedisplay.run()

        