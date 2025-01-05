import tkinter as tk

class DifficultySelector:
    def __init__(self, controller):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Select Difficulty")
        self.window.geometry("400x300")  

        self.easy_button = tk.Button(self.window, text="Facile", command=self.set_easy, width=20, height=2)
        self.medium_button = tk.Button(self.window, text="Moyen", command=self.set_medium, width=20, height=2)
        self.hard_button = tk.Button(self.window, text="Difficile", command=self.set_hard, width=20, height=2)

        self.easy_button.pack(pady=20)
        self.medium_button.pack(pady=20)
        self.hard_button.pack(pady=20)

        window_width = 400
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)

        self.window.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

        self.window.attributes("-topmost", True)

    def set_easy(self):
        self.controller.difficulty = "Facile"
        self.window.destroy()

    def set_medium(self):
        self.controller.difficulty = "Moyen"
        self.window.destroy()

    def set_hard(self):
        self.controller.difficulty = "Difficile"
        self.window.destroy()

    def display_difficulties(self):
        self.window.mainloop()
