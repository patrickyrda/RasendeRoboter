from .board import Board, obstacles
from .robot import Robot 
import random
# have to crete init state function that will set variables of robot positions and target
# TODO: TESTE IF THE HAS AND EQ ARE WORKING, i think they are but in case 

class State:

    def __init__(self, board : Board, Rrobot : Robot, Grobot : Robot, Brobot : Robot, Yrobot : Robot, target : tuple[int, int], color : int):
        self.board = board
        self.robots = [Rrobot, Grobot, Brobot, Yrobot]
        self.target = target

        self.target_color = color

        # A* variables, g is initialized with 40 but then replaced inside of the A*
        self.g = 40 
        self.h = 0
        self.f = 0
        self.parent = None
         
    def get_robot_coords(self, target_robot=None) -> tuple:

        if target_robot is None:
            return tuple((robot.x, robot.y) for robot in self.robots)
        
        return (self.robots[self.target_color].x, self.robots[self.target_color].y)
    
    # TODO: THOSE ONES WORKED BETTER FOR THE GREEDY BFS 
    def __hash__(self):
        return hash(self.get_robot_coords())
    
    def __eq__(self, other):
        # Maybe can complete here to further eliminate useless states like the ones where secondary robots switched places !!!!!!
        if not isinstance(other, State):
            return False
        return self.get_robot_coords() == other.get_robot_coords()
    
    def __lt__(self, other):
        return self.f < other.f    
    '''
    def _cmp_key(self):
        result = f"{self.f:02}"
        result += "".join(f"{x:02}{y:02}" for x, y in self.get_robot_coords())
        # print("\n", result)
        return result
    
    def __hash__(self):
        return hash(self._cmp_key())
    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self._cmp_key() == other._cmp_key()
    def __lt__(self, other):
        return self._cmp_key() < other._cmp_key()

    # TODO : USE ONLY A SINGLE FUNCTION, LIKE IN THE ROBOT CLASS, AND USE THE ROBOTS MOVE FUNCTION INSIDE OF IT SINCE THE CODE IS BASICALLY THE SAME AND IT RETURNS COORDS
    '''
    def slide_robot_right(self, robot : Robot):
        """
        This function moves the robot to the right as much as possible, given the obstacles present on the board.
        It will stop when it hits a barrier or another robot. 

        Parameters:
        robot (Robot): The robot to move

        Returns:
        None
        """
        stop = False
        starty = robot.y
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"]] or robot.y == 15 or self.board.board[robot.x][robot.y + 1].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x][robot.y + 1].has_robot != 10:
                stop = True
            else:
                robot.y += 1
        self.board.board[robot.x][starty].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.idx
        

    def slide_robot_left(self, robot : Robot):
        """
        This function moves the robot to the left as much as possible, given the obstacles present on the board.
        It will stop when it hits a barrier or another robot.

        Parameters:
        robot (Robot): The robot to move

        Returns:
        None
        """
        stop = False
        starty = robot.y
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"]] or robot.y == 0 or self.board.board[robot.x][robot.y - 1].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x][robot.y - 1].has_robot != 10:
                stop = True
            else:
                robot.y -= 1
        self.board.board[robot.x][starty].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.idx

    def slide_robot_down(self, robot : Robot):
        """
        This function moves the robot down as much as possible, given the obstacles present on the board.
        It will stop when it hits a barrier or another robot.

        Parameters:
        robot (Robot): The robot to move

        Returns:
        None
        """
        stop = False
        startx = robot.x
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"]] or robot.x == 15 or self.board.board[robot.x + 1][robot.y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x + 1][robot.y].has_robot != 10:
                stop = True
            else:
                robot.x += 1
        self.board.board[startx][robot.y].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.idx

    def slide_robot_up(self, robot : Robot):
        """
        This function moves the robot up as much as possible, given the obstacles present on the board.
        It will stop when it hits a barrier or another robot.

        Parameters:
        robot (Robot): The robot to move

        Returns:
        None
        """
        stop = False
        startx = robot.x
        while not stop:
            if self.board.board[robot.x][robot.y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"]] or robot.x == 0 or self.board.board[robot.x - 1][robot.y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"], obstacles["Middle_Barrier"]] or self.board.board[robot.x - 1][robot.y].has_robot != 10:
                stop = True
            else:
                robot.x -= 1
        self.board.board[startx][robot.y].has_robot = 10
        self.board.board[robot.x][robot.y].has_robot = robot.idx

    def check_setup(self):
        """
        Assign the robots positions to the board has_robot attribute
        Check is used to represent the initial position of the robots
        """
        for robot in self.robots:
            self.board.board[robot.x][robot.y].has_robot = robot.idx
            self.board.board[robot.x][robot.y].check = 1  
            # TODO: CANT FORGT TO MOVE THE .CHECK FROM THE CODE, AND ADD HERE IN THE INIT OF THE OBECT

    def set_as(self, g, h, parent) -> None:
        """
        Set the A* values of the state.

        Parameters:
        g (int): The cost of the path from the initial state to this state.
        h (int): The heuristic value of this state.
        parent (State): The parent state of this state.

        Returns:
        None
        """
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def places_robots_random(self):
        
        for robot in self.robots:
            placed = False
            while not placed:
                x = random.randint(0, 15)
                y = random.randint(0, 15)

                ogx, ogy = robot.get_coord()
                
                if self.board.board[x][y].val != obstacles["Middle_Barrier"] and self.board.board[x][y].has_robot == 10:
                    self.board.board[x][y].has_robot = robot.idx
                    self.board.board[ogx][ogy].has_robot = 10
                    robot.x = x
                    robot.y = y
                    placed = True
    
    def place_taget_random(self):
        placed = False
        while not placed:
            x = random.randint(0, 15)
            y = random.randint(0, 15)
            if self.board.board[x][y].val != obstacles["Middle_Barrier"] and self.board.board[x][y].has_robot == 10 and self.board.board[x][y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"], obstacles["B_L_Barrier"], obstacles["B_R_Barrier"]]:
                self.board.board[x][y].has_robot = 10
                self.target = (x, y)
                placed = True
        
        self.target_color = random.randint(0, 3)


    def change_state(self):
        self.places_robots_random()
        self.place_taget_random()
        self.set_as(40, 0, None)
