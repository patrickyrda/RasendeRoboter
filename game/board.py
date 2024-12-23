import numpy as np
from collections import deque
from colorama import Fore, Style, init
obstacles = {
    "T_L_Barrier" : 1,
    "T_R_Barrier" : 2,
    "B_L_Barrier" : 3,
    "B_R_Barrier" : 4,
    "Middle_Barrier" : 5,
}

 # TODO SIMPLIFY THE HERUSTICS FUNCTION 
class Node:
    def __init__(self, val = 0, has_robot= 0, has_target= 11, check = 0):

        self.val = val
        self.has_robot = has_robot
        self.has_target = has_target  
        self.check = check


class Board:
    def __init__(self):
        
        self.board = [[Node() for _ in range(16)] for _ in range(16)]
        
        self.board[0][1].val = obstacles["T_R_Barrier"]
        self.board[0][11].val = obstacles["T_R_Barrier"]
        self.board[1][4].val = obstacles["T_R_Barrier"]
        self.board[1][13].val = obstacles["T_L_Barrier"]
        self.board[2][9].val = obstacles["T_R_Barrier"]
        self.board[3][1].val = obstacles["B_L_Barrier"]
        self.board[3][11].val = obstacles["B_L_Barrier"]
        self.board[5][0].val = obstacles["B_L_Barrier"]
        self.board[5][5].val = obstacles["T_L_Barrier"]
        self.board[5][14].val = obstacles["B_L_Barrier"]
        self.board[6][3].val = obstacles["B_R_Barrier"]
        self.board[6][11].val = obstacles["T_R_Barrier"]
        self.board[8][5].val = obstacles["B_L_Barrier"]
        self.board[9][2].val = obstacles["T_L_Barrier"]
        self.board[9][12].val = obstacles["T_R_Barrier"]
        self.board[10][15].val = obstacles["T_R_Barrier"]
        self.board[11][0].val = obstacles["B_L_Barrier"]
        self.board[12][9].val = obstacles["T_L_Barrier"]
        self.board[13][4].val = obstacles["T_R_Barrier"]
        self.board[13][14].val = obstacles["B_L_Barrier"]
        self.board[14][1].val = obstacles["B_R_Barrier"]
        self.board[14][11].val = obstacles["B_R_Barrier"]
        self.board[15][5].val = obstacles["B_R_Barrier"]
        self.board[15][14].val = obstacles["B_L_Barrier"]

        self.board[6][11].has_target = 1

        self.board1 = [[self.board[i][j].val for j in range(8)] for i in range(8)]
        self.board2 = [[self.board[i][j+8].val for j in range(8)] for i in range(8)]
        self.board3 = [[self.board[i+8][j].val for j in range(8)] for i in range(8)]
        self.board4 = [[self.board[i+8][j+8].val for j in range(8)] for i in range(8)]
        
        


        
    
        
    def turn_board(self,tab):
        nb_rotation = random.randint(0,3)
        for r in range(nb_rotation):
            self.boardt = [[self.tab[i][j].val for j in range(8)] for i in range(8)]
            for i in range(8):
                for j in range(8):
                    self.tab[i][j].val = self.boardt[8-j-1][i].val
                    if self.tab[i][j].val == obstacles["T_L_Barrier"] :
                        self.tab[i][j].val = obstacles["T_R_Barrier"]
                    elif self.tab[i][j].val == obstacles["T_R_Barrier"] :
                        self.tab[i][j].val = obstacles["B_R_Barrier"]
                    elif self.tab[i][j].val == obstacles["B_R_Barrier"] :
                        self.tab[i][j].val = obstacles["B_L_Barrier"]
                    elif self.tab[i][j].val == obstacles["B_L_Barrier"] :
                        self.tab[i][j].val = obstacles["T_L_Barrier"]
        return self


    def assemble_pieces(self):
        # assemble boardpieces
        for i in range(8):
            for j in range(8):
                self.board[i][j] = self.board1[i][j]
        for i in range(8):
            for j in range(8):
                self.board[i][j+8] = self.board2[i][j]
        for i in range(8):
            for j in range(8):
                self.board[i+8][j] = self.board3[i][j]
        for i in range(8):
            for j in range(8):
                self.board[i+8][j+8] = self.board4[i][j]
        self.board[7][7].val = obstacles["Middle_Barrier"]
        self.board[7][8].val = obstacles["Middle_Barrier"]
        self.board[8][7].val = obstacles["Middle_Barrier"]
        self.board[8][8].val = obstacles["Middle_Barrier"]
        return self
    
    def heuristics_board(self, a : int, b: int) -> list[list[int]]:
        '''
        Functions that determines the heuristics board from the board and returns this board
        Takes the initial row position a and the initial col position b as arguments
        returns a 2D list of the heuristics board
        '''
        result_board = np.zeros((16,16), dtype=int)
        result_board[a][b] = 111
        ongoing = True
        distance = 0
        pos_buffer = deque([(a, b)])
        while(ongoing):
            distance += 1
            tmp_pos_buffer = deque()
            while (pos_buffer):
                x, y = pos_buffer.popleft() 
                # movement from initial position to up 
                for i in range (x, 0, -1):
                    if (self.board[i - 1][y].val == obstacles["B_L_Barrier"] or self.board[i - 1][y].val == obstacles["B_R_Barrier"] or self.board[i - 1][y].val == obstacles["Middle_Barrier"]) or self.board[i][y].val in [obstacles["T_L_Barrier"], obstacles["T_R_Barrier"]]:
                        break
                    elif (self.board[i - 1][y].val == obstacles["T_L_Barrier"] or self.board[i - 1][y].val == obstacles["T_R_Barrier"]):
                        if (result_board[i - 1][y] == 0):
                            result_board[i - 1][y] = distance
                            tmp_pos_buffer.append((i - 1, y))
                        break
                    else:
                        if (result_board[i - 1][y] == 0):
                            result_board[i - 1][y] = distance
                            tmp_pos_buffer.append((i - 1, y))
                # movement from initial position to down
                for i in range(x, 15, 1):
                    if (self.board[i + 1][y].val == obstacles["T_L_Barrier"] or self.board[i + 1][y].val == obstacles["T_R_Barrier"] or self.board[i + 1][y].val == obstacles["Middle_Barrier"]) or self.board[i][y].val in [obstacles["B_L_Barrier"], obstacles["B_R_Barrier"]]:
                        break
                    elif (self.board[i + 1][y].val == obstacles["B_L_Barrier"] or self.board[i + 1][y].val == obstacles["B_R_Barrier"]):
                        if (result_board[i + 1][y] == 0):    
                            result_board[i + 1][y] = distance
                            tmp_pos_buffer.append((i + 1, y))
                        break
                    else:
                        if (result_board[i + 1][y] == 0):    
                            result_board[i + 1][y] = distance
                            tmp_pos_buffer.append((i + 1, y))
                # movement from initial position to left
                
                for i in range(y, 0, -1):
                    if (self.board[x][i - 1].val == obstacles["T_R_Barrier"] or self.board[x][i - 1].val == obstacles["B_R_Barrier"] or self.board[x][i - 1].val == obstacles["Middle_Barrier"]) or self.board[x][i].val in [obstacles["T_L_Barrier"], obstacles["B_L_Barrier"]]:
                        break
                    elif (self.board[x][i - 1].val == obstacles["T_L_Barrier"] or self.board[x][i - 1].val == obstacles["B_L_Barrier"]):
                        if (result_board[x][i - 1] == 0):      
                            result_board[x][i - 1] = distance
                            tmp_pos_buffer.append((x, i - 1))
                        break
                    else:
                        if (result_board[x][i - 1] == 0): 
                            tmp_pos_buffer.append((x, i - 1))
                            result_board[x][i - 1] = distance
                # movement from initial position to right
                
                for i in range(y, 15, 1):
                    if (self.board[x][i + 1].val == obstacles["T_L_Barrier"] or self.board[x][i + 1].val == obstacles["B_L_Barrier"] or self.board[x][i + 1].val == obstacles["Middle_Barrier"]) or self.board[x][i].val in [obstacles["T_R_Barrier"], obstacles["B_R_Barrier"]]:
                        break
                    elif (self.board[x][i + 1].val == obstacles["T_R_Barrier"] or self.board[x][i + 1].val == obstacles["B_R_Barrier"]):
                        if (result_board[x][i + 1] == 0):   
                            result_board[x][i + 1] = distance
                            tmp_pos_buffer.append((x, i + 1))   
                        break
                    else:
                        if (result_board[x][i + 1] == 0):   
                            tmp_pos_buffer.append((x, i + 1))   
                            result_board[x][i + 1] = distance
            
            pos_buffer = tmp_pos_buffer

            if (len(pos_buffer) == 0):
                ongoing = False

        result_board[a][b] = 0
        return result_board
    
    def print_board(self):
        '''
        Print the board with colors
        '''
        for row in self.board:
            print(" ".join(
                f"{Fore.MAGENTA}S{Style.RESET_ALL}" if node.check == 1 else
                f"{Fore.RED}R{Style.RESET_ALL}" if node.has_robot == 0 else
                f"{Fore.GREEN}G{Style.RESET_ALL}" if node.has_robot == 1 else
                f"{Fore.BLUE}B{Style.RESET_ALL}" if node.has_robot == 2 else
                f"{Fore.YELLOW}Y{Style.RESET_ALL}" if node.has_robot == 3 else
                str(node.val)
                for node in row
            ))


                    


                
                






        



        




