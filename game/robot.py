from .board import obstacles
from .board import Node
colors = {
    "red": 0,
    "green": 1,
    "blue": 2,
    "yellow": 3
}
# TODO: HAVE ONLY ONE FUNCTION FOR ALL USING PARAMETERS TO CHANGE DIRECTIONS 

class Robot:
    def __init__(self, color : int, x : int, y : int):
        self.x = x
        self.y = y
        self.color = color
    # TODO : have to add here control to check if there is no robot in the postion DONE , have to test!!!!!!!!!!!!
    def move_right(self, tab) -> tuple[int, int]:
        
        stop = False
        x , y = self.x, self.y
        while not stop:
            if tab[x][y].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"]] or y == 15 or tab[x][y + 1].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"], obstacles["Middle_Barrier"]] or tab[x][y + 1].has_robot != 10:
                stop = True
            else:
                y += 1
        return x, y

    def move_left(self, tab) -> tuple[int, int]:
        stop = False
        x , y = self.x, self.y
        while not stop:
            if tab[x][y].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"]] or y == 0 or tab[x][y - 1].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"], obstacles["Middle_Barrier"]] or tab[x][y - 1].has_robot != 10:
                stop = True
            else:
                y -= 1
        
        return x, y


    def move_down(self, tab) -> tuple[int, int]:
        stop = False
        x , y = self.x, self.y
        while not stop:
            if tab[x][y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"]] or x == 15 or tab[x + 1][y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"], obstacles["Middle_Barrier"]] or tab[x + 1][y].has_robot != 10:
                stop = True
            else:
                x += 1

        return x, y
    def move_up(self, tab):
        stop = False
        x , y = self.x, self.y
        while not stop:
            if tab[x][y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"]] or x == 0 or tab[x - 1][y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"], obstacles["Middle_Barrier"]] or tab[x - 1][y].has_robot != 10:
                stop = True
            else:
                x -= 1
        return x, y    
   