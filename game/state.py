from .board import Board, obstacles
from .robot import Robot 
# have to crete init state function that will set variables of robot positions and target


class State:

    def __init__(self, board : Board, Rrobot : Robot, Grobot : Robot, Brobot : Robot, Yrobot : Robot, target : tuple[int, int], color : int):
        self.board = board
        self.robots = [Rrobot, Grobot, Brobot, Yrobot]
        self.target = target
        self.target_color = color
         
    def place_robot_random(self):
        # place robot in random position
        for robot in self.robots :
            place = 0
            while(place==0):
                i = random.randint(0,15)
                j = random.randint(0,15)
                if self.board[i][j].has_robot == 10 :
                    tab[i][j].has_robot = robot
                    place = 1
        return 
    
    def get_robot_coords(self) -> tuple:
        return tuple((robot.x, robot.y) for robot in self.robots)
        
    def __hash__(self):
        return hash(self.get_robot_coords())

    def __eq__(self, other):
        # Maybe can complete here to further eliminate useless states like the ones where secondary robots switched places !!!!!!
        if not isinstance(other, State):
            return False
        return self.get_robot_coords() == other.get_robot_coords()

    

    # TODO : USE ONLY A SINGLE FUNCTION, LIKE IN THE ROBOT CLASS, AND USE THE ROBOTS MOVE FUNCTION INSIDE OF IT SINCE THE CODE IS BASICALLY THE SAME AND IT RETURNS COORDS

    def slide_robot_right(self, robot : Robot):
        
        stop = False
        starty = robot.y
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"]] or robot.y == 15 or self.board.board[robot.x][robot.y + 1].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x][robot.y + 1].has_robot != 10:
                stop = True
            else:
                robot.y += 1
        self.board.board[robot.x][starty].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.color
        

    def slide_robot_left(self, robot : Robot):
        stop = False
        starty = robot.y
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"]] or robot.y == 0 or self.board.board[robot.x][robot.y - 1].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x][robot.y - 1].has_robot != 10:
                stop = True
            else:
                robot.y -= 1
        self.board.board[robot.x][starty].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.color

    def slide_robot_down(self, robot : Robot):

        stop = False
        startx = robot.x
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"]] or robot.x == 15 or self.board.board[robot.x + 1][robot.y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x + 1][robot.y].has_robot != 10:
                stop = True
            else:
                robot.x += 1
        self.board.board[startx][robot.y].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.color

    def slide_robot_up(self, robot : Robot):
        stop = False
        startx = robot.x
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"]] or robot.x == 0 or self.board.board[robot.x - 1][robot.y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x - 1][robot.y].has_robot != 10:
                stop = True
            else:
                robot.x -= 1
        self.board.board[startx][robot.y].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.color

    def check_setup(self):
        for robot in self.robots:
            self.board.board[robot.x][robot.y].has_robot = robot.color
            self.board.board[robot.x][robot.y].check = 1  
            # TODO: CANT FORGT TO MOVE THE .CHECK FROM THE CODE 
