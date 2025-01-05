import tkinter as tk
from algorithms.bfs import bfs
from game.board import Board, obstacles
from game.robot import Robot
from game.state import State
from tkinter import Toplevel



# Dictionnaire de couleurs pour représenter les différents éléments du plateau
COLORS = {
    "empty": "#f4f4f4",           # Case vide
    "robot": "red",               # Couleur temporaire pour les robots (sera remplacée par la couleur des robots)
    "target": "#4CAF50",          # Couleur pour la cible (vert)
    "Middle_Barrier": "#BDBDBD",  # Barrière au centre
}

class RobotGame:
    def __init__(self, state, difficulty="none"):
        self.root1 = tk.Tk()
        self.difficulty = difficulty  # Récupérer la difficulté choisie
        self.root1.title("Rasende Roboter")

        # Taille des cellules et du canvas
        self.cell_size = 40
        self.canvas_size = 16 * self.cell_size

        # Initialisation du plateau et des robots
        self.state = state

        # Initialisation des variables du jeu
        self.selected_robot = None
        self.possible_moves = []
        self.move_counter = 0
        self.robot_red = self.state.robots[0]
        self.game_active = False  # Le jeu n'est pas encore activé
        self.victory_label = None
        self.timer_label = None  # Label pour afficher le timer
        self.timer_seconds = 90  # 1 minute 30 secondes

        # Création des frames
        self._create_frames()

        # Création du canvas
        self.canvas = tk.Canvas(self.game_frame, width=self.canvas_size, height=self.canvas_size, bg="#E0E0E0")
        self.canvas.pack()
        self.counter_label = tk.Label(self.counter_frame, text=f"Moves: {self.move_counter}", font=("Arial", 16, "bold"), bg="#FFFFFF")
        self.counter_label.pack()

        # Cacher tous les éléments du jeu au départ
        self.counter_label.pack_forget()
        self.timer_label.pack_forget()
        self.start_button.pack_forget()

        self.has_won = False

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

        # Add more initialization here...
    def _create_frames(self):
        self.main_frame = tk.Frame(self.root1, bg="#F0F0F0")
        self.main_frame.pack(padx=20, pady=20)

        self.game_frame = tk.Frame(self.main_frame)
        self.game_frame.pack(side="left", padx=10)

        self.counter_frame = tk.Frame(self.main_frame, bd=2, relief="groove", padx=10, pady=10, bg="#FFFFFF")
        self.counter_frame.pack(side="left", padx=20)

        # Création du bouton "Start" au-dessus du compteur
        self.start_button = tk.Button(self.counter_frame, text="Start", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=10)

        # Création du label pour le timer
        self.timer_label = tk.Label(self.counter_frame, text=f"Time: {self.timer_seconds // 60}:{self.timer_seconds % 60:02d}", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        # Création du label "Coup Estimé" et la Spinbox
        self.estimated_move_label = tk.Label(self.counter_frame, text="Coup Estimé:", font=("Arial", 14))
        self.estimated_move_spinbox = tk.Spinbox(self.counter_frame, from_=1, to=25, font=("Arial", 14), width=5)

        # Création du bouton "Valider"
        self.validate_button = tk.Button(self.counter_frame, text="Valider", font=("Arial", 14), command=self.validate_action)

        # Affichage initial de la Spinbox et du bouton "Valider"
        self.estimated_move_label.pack(pady=5)
        self.estimated_move_spinbox.pack(pady=5)
        self.validate_button.pack(pady=10)

    def validate_action(self):

        self.estimated_move = self.estimated_move_spinbox.get()
        self.estimated_move_label.pack_forget()
        self.estimated_move_spinbox.pack_forget()
        self.validate_button.pack_forget()

        # Afficher le timer, le compteur, et le bouton Start
        self.counter_label.pack(pady=10)
        self.timer_label.pack(pady=10)
        self.start_button.pack(pady=10)

        # Démarrer le jeu (Activer le bouton start et démarrer le timer)
        self.start_button.config(state="normal")

    def start_game(self):
        """Active le jeu et démarre le compte à rebours du timer."""
        self.game_active = True # Le jeu commence maintenant

        self.start_button.config(state="disabled")  # Désactive le bouton Start une fois qu'il a été cliqué
        self.start_timer()  # Démarre le timer

    def start_timer(self):
        """Démarre le compte à rebours du timer."""
        if self.timer_seconds > 0 and self.game_active:
            minutes = self.timer_seconds // 60
            seconds = self.timer_seconds % 60
            self.timer_label.config(text=f"Time: {minutes}:{seconds:02d}")
            self.timer_seconds -= 1
            # Met à jour le timer toutes les 1000 ms (1 seconde)
            self.root1.after(1000, self.start_timer)
        else:
            if self.game_active:  # Si le temps est écoulé et que le jeu est encore actif, afficher "LOSER"
                self.end_game("LOSER")  # Arrête le jeu et affiche "LOSER"
                self.start_button.config(state="disabled")  # Désactive le bouton Start à la fin du jeu


    def end_game(self, message):
        """Arrête le jeu et affiche un message de fin."""
        self.game_active = False
        self.start_button.config(state="disabled")  # Désactive le bouton Start à la fin du jeu

        if message == "You couldn't verify your guess! Now the AI is gonna calculate its answer":
            self.show_message_window(message)
            self.root1.destroy()
        else:
            final_message = f"{message}\nCoup estimé : {self.estimated_move}"
            self.timer_label.config(text=final_message)
            self.show_message_window("You verified your guess, now the AI is gonna calculate its answer")
            self.root1.destroy()

    def draw_board(self):
        self.canvas.delete("all")

        # Dessiner les cases et obstacles
        for i in range(16):
            for j in range(16):
                self._draw_cell(i, j)

        # Dessiner les robots
        for robot in self.state.robots:
            self._draw_robot(robot)

        # Dessiner les mouvements possibles
        for move in self.possible_moves:
            self._highlight_move(move)

    def _draw_cell(self, i, j):
        x1, y1 = j * self.cell_size, i * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        node = self.state.board.board[i][j]
        color = COLORS["empty"]

        if (i, j) == self.state.target:  # Coloration de la cible
            color = COLORS["target"]
        elif node.val == obstacles["Middle_Barrier"]:
            color = COLORS["Middle_Barrier"]

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        self._draw_obstacles(x1, y1, x2, y2, node)

    def _draw_obstacles(self, x1, y1, x2, y2, node):
        """Dessine les lignes de barrières selon leur type."""
        if node.val == obstacles["T_L_Barrier"]:
            self.canvas.create_line(x1, y1, x1, y2, width=2, fill="black")
            self.canvas.create_line(x1, y1, x2, y1, width=2, fill="black")
        elif node.val == obstacles["T_R_Barrier"]:
            self.canvas.create_line(x2, y1, x2, y2, width=2, fill="black")
            self.canvas.create_line(x1, y1, x2, y1, width=2, fill="black")
        elif node.val == obstacles["B_L_Barrier"]:
            self.canvas.create_line(x1, y2, x1, y1, width=2, fill="black")
            self.canvas.create_line(x1, y2, x2, y2, width=2, fill="black")
        elif node.val == obstacles["B_R_Barrier"]:
            self.canvas.create_line(x2, y2, x2, y1, width=2, fill="black")
            self.canvas.create_line(x1, y2, x2, y2, width=2, fill="black")

    def _draw_robot(self, robot):
        robot_x = (robot.y * self.cell_size) + self.cell_size // 2
        robot_y = (robot.x * self.cell_size) + self.cell_size // 2
        self.canvas.create_oval(robot_x - 10, robot_y - 10, robot_x + 10, robot_y + 10, fill=robot.color, outline="black")

    def _highlight_move(self, move):
        x, y = move
        x1, y1 = y * self.cell_size, x * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")

    def on_click(self, event):
        if not self.game_active:
            return
        row, col = event.y // self.cell_size, event.x // self.cell_size

        clicked_robot = next((r for r in self.state.robots if r.x == row and r.y == col), None)

        if clicked_robot:
            self.selected_robot = clicked_robot
            self.calculate_possible_moves(clicked_robot)
        elif (row, col) in self.possible_moves and self.selected_robot:
            self.move_robot(self.selected_robot, row, col)
            self.selected_robot = None
            self.possible_moves = []

        self.draw_board()

    def calculate_possible_moves(self, robot):
        self.possible_moves = []
        directions = [robot.move_right, robot.move_left, robot.move_down, robot.move_up]
        for move in directions:
            new_x, new_y = move(self.state.board.board)
            if (new_x, new_y) != (robot.x, robot.y):
                self.possible_moves.append((new_x, new_y))
    def show_message_window(self, message):
    # Crée une petite fenêtre pop-up
        message_window = tk.Toplevel(self.root1)
        message_window.title("Game Over")
        message_window.geometry("600x200")
        
        # Label pour afficher le message
        message_label = tk.Label(message_window, text=message, font=("Arial", 14), fg="red")
        message_label.pack(pady=20)

        # Bouton pour fermer la fenêtre
        close_button = tk.Button(message_window, text="Close", font=("Arial", 12), command=message_window.destroy)
        close_button.pack()

        # Empêche toute interaction avec la fenêtre principale pendant que la fenêtre pop-up est ouverte
        message_window.transient(self.root1)
        message_window.grab_set()
        self.root1.wait_window(message_window)

    def move_robot(self, robot, new_x, new_y):
        # Vérifier si le nombre de coups dépasse l'estimation
        if self.move_counter >= int(self.estimated_move):
            self.end_game("You couldn't verify your guess! Now the AI is gonna calculate its answer")
            return

        # Marque l'ancienne position comme vide
        self.state.board.board[robot.x][robot.y].has_robot = 10
        # Déplace le robot
        robot.x, robot.y = new_x, new_y
        # Marque la nouvelle position du robot
        self.state.board.board[new_x][new_y].has_robot = robot.color

        # Incrémente le compteur de déplacements à chaque mouvement d'un robot
        self.move_counter += 1
        self.counter_label.config(text=f"Moves: {self.move_counter}")

        # Vérifie si le robot rouge a atteint la cible pour afficher un message de victoire
        if robot == self.robot_red and (new_x, new_y) == self.state.target:
            self.end_game("VICTORY!")  # Affiche "VICTORY!" si la solution est trouvée
            self.has_won = True
            self.start_button.config(state="disabled")  # Désactive le bouton Start à la fin du jeu



    def display(self):
        self.root1.mainloop()

    


