import os
import tkinter as tk

class StateDisplayer:
    def __init__(self, root, state_list, canvas_size=500, cell_size=30):

        self.root = root
        self.state_list = state_list  # List of all states to display
        self.current_index = 0  # To track the current state being displayed
        self.canvas_size = canvas_size
        self.cell_size = cell_size

        # Create the frames
        self._create_frames()

        # Display the first state
        self.display_state(self.state_list[self.current_index])
        self.title_label = tk.Label(self.root, text="AI Solution", font=("Arial", 18, "bold"), bg="#F0F0F0")
        self.title_label.pack(pady=10)
        self.title_label.place(relx=0.95, rely=0.05, anchor="ne")

        self.ai_label = tk.Label(self.counter_frame, text=f"Play amount of AI: {len(self.state_list) - 1}", font=("Arial", 12))
        self.ai_label.pack(pady=10)

    def _create_frames(self):
        """Create the main frames for the UI."""
        self.main_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.main_frame.pack(padx=20, pady=20)

        self.game_frame = tk.Frame(self.main_frame)
        self.game_frame.pack(side="left", padx=10)

        self.counter_frame = tk.Frame(self.main_frame, bd=2, relief="groove", padx=10, pady=10, bg="#FFFFFF")
        self.counter_frame.pack(side="left", padx=20)

        # Create the "Next State" button
        self.next_button = tk.Button(self.counter_frame, text="Next State", font=("Arial", 14), command=self.next_state)
        self.next_button.pack(pady=10)

        # Create the canvas for drawing the state
        self.canvas = tk.Canvas(self.game_frame, width=self.canvas_size, height=self.canvas_size, bg="#E0E0E0")
        self.canvas.pack()

        # Ajouter le bouton "Rejouer" au-dessus du bouton "Quit"
        self.restart_button = tk.Button(self.counter_frame, text="Rejouer", font=("Arial", 14), command=self.restart_game)
        self.restart_button.pack(pady=10)

        # Masquer le bouton "Rejouer" initialement
        self.restart_button.pack_forget()



    def display_state(self, state):
        """Display the current state on the canvas."""
        self.canvas.delete("all")  # Clear the canvas before drawing the new state

        # Draw the cells and obstacles
        for i in range(16):
            for j in range(16):
                self._draw_cell(i, j, state)

        # Draw the robots
        for robot in state.robots:
            self._draw_robot(robot)

    def _draw_cell(self, i, j, state):
        """Draw a single cell in the grid."""
        x1, y1 = j * self.cell_size, i * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        node = state.board.board[i][j]
        color = "#FFFFFF"  # Default color for empty cells

        if (i, j) == state.target:  # Target cell
            color = "purple"
        elif node.val == "Middle_Barrier":  # Example obstacle
            color = "#000000"

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def _draw_robot(self, robot):
        """Draw a robot on the canvas."""
        robot_x = (robot.y * self.cell_size) + self.cell_size // 2
        robot_y = (robot.x * self.cell_size) + self.cell_size // 2
        self.canvas.create_oval(robot_x - 10, robot_y - 10, robot_x + 10, robot_y + 10, fill=robot.color, outline="black")

    def next_state(self):
        """Go to the next state in the list or quit if at the end."""
        self.current_index += 1
        if self.current_index >= len(self.state_list):
            self.current_index = len(self.state_list) - 1  # Stay at the last state
            self.next_button.config(text="Quit", command=self.quit_game)  # Change button to "Quit"
            self.show_restart_button()  # Afficher le bouton "Rejouer"

        else:
            self.display_state(self.state_list[self.current_index])

    def show_restart_button(self):
        """Afficher le bouton "Rejouer" lorsque le bouton "Quit" est visible."""
        self.restart_button.pack()  # Afficher le bouton "Rejouer"

    def restart_game(self):
        """Redémarrer le jeu en fermant la fenêtre actuelle et en relançant le jeu."""
        self.root.quit()  # Fermer la fenêtre actuelle
        self.root.destroy()
        os.system('python main.py')# Appeler la fonction main pour relancer le jeu

    def quit_game(self):
        """Quit the game and close the window."""
        self.root.quit()

    def run(self):
        """Start the GUI event loop."""
        self.root.mainloop()

