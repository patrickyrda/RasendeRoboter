class Robot:
    def __init__(self, color:str, x: int, y: int):
        self.color = color                        #Here option to use numbers as code, WHICH I THINK IS THE BEST IDEA, or leave the color as a string 
        self.x = x
        self.y = y

    
    def robot_move_right(tab,robot):
    for i in range(16):
        for j in range(16):
            if tab[i][j][1] == robot :
                x = i
                y = j
    stop = 0
    original_y = y
    while stop == 0 :
        if tab[x][y][0] == 2 or tab[x][y][0] == 3 or y == 15 or tab[x][y+1][0] == 1 or tab[x][y+1][0] == 4 :
            stop = 1
        else :
            y = y+1
    tab[x][original_y][1] = 0
    tab[x][y][1] = robot

def robot_move_left(tab,robot):
    for i in range(16):
        for j in range(16):
            if tab[i][j][1] == robot :
                x = i
                y = j
    stop = 0
    original_y = y
    while stop == 0 :
        if tab[x][y][0] == 1 or tab[x][y][0] == 4 or y == 0 or tab[x][y-1][0] == 2 or tab[x][y-1][0] == 3 :
            stop = 1
        else :
            y = y-1
    tab[x][original_y][1] = 0
    tab[x][y][1] = robot
    
def robot_move_down(tab,robot):
    for i in range(16):
        for j in range(16):
            if tab[i][j][1] == robot :
                x = i
                y = j
    stop = 0
    original_x = x
    while stop == 0 :
        if tab[x][y][0] == 3 or tab[x][y][0] == 4 or x == 15 or tab[x+1][y][0] == 1 or tab[x+1][y][0] == 2 :
            stop = 1
        else :
            x = x+1
    tab[original_x][y][1] = 0
    tab[x][y][1] = robot


def robot_move_top(tab,robot):
    for i in range(16):
        for j in range(16):
            if tab[i][j][1] == robot :
                x = i
                y = j
    stop = 0
    original_x = x
    while stop == 0 :
        if tab[x][y][0] == 1 or tab[x][y][0] == 2 or x == 0 or tab[x-1][y][0] == 3 or tab[x-1][y][0] == 4 :
            stop = 1
        else :
            x = x-1
    tab[original_x][y][1] = 0
    tab[x][y][1] = robot

   
