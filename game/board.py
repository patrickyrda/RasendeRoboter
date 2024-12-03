from boardpiece import BoardPiece
from robot import Robot
import numpy as np
import copy
import random
'''
Top Left barrier = 1
Top Right barrier = 2
Down Right barrier = 3
Down Left barrier = 4
Green robot = 1
Red robot = 2
Blue robot = 3
Yellow robot = 4
Green target = 5
Red target = 6
Blue target = 7
Yellow target = 8
middle block = 9
'''
class Board:
    def turn_board(tab,nb_rotation):
        for r in range(nb_rotation):
            tmp_tab = copy.deepcopy(tab)
            for i in range(8):
                for j in range(8):
                    tab[i][j] = tmp_tab[8-j-1][i]
                    if tab[i][j][0] != 0 :
                        tab[i][j][0] += 1
                    if tab[i][j][0] == 5 :
                        tab[i][j][0] = 1
        return tab

    
    def place_robot_random(tab):
        # place robot in random position
        for i in range(4):
            place = 0
            while(place==0):
                i = random.randint(1,16)
                j = random.randint(1,16)
                if tab[i][j][1]==0 :
                    tab[i][j][1] = i+1
        return tab
        
        
    def assemble_pieces(tab1,tab2,tab3,tab4):
        # assemble boardpieces
        tab = [[[0, 0] for _ in range(16)] for _ in range(16)]
        for i in range(8):
            for j in range(8):
                tab[i][j] = tab1[i][j]
        for i in range(8):
            for j in range(8):
                tab[i][j+8] = tab2[i][j]
        for i in range(8):
            for j in range(8):
                tab[i+8][j] = tab4[i][j]
        for i in range(8):
            for j in range(8):
                tab[i+8][j+8] = tab3[i][j]
        tab[7][7][0]=1
        tab[7][8][0]=2
        tab[8][8][0]=3
        tab[8][7][0]=4
        tab[7][7][1]=tab[7][8][1]=tab[8][8][1]=tab[8][7][1]=9
        return tab
        

    def change_target(tab):
        # place targets in random positions of the board once it has been assembled
        liste = []
        for i in range(16):
            for j in range(16):
                if tab[i][j][0] != 0 and tab[i][j][1] == 0 :
                    liste.append([i,j])
                if tab[i][j][1] != 9 and tab[i][j][1] > 4 :
                    tab[i][j][1] = 0
        x = random.randint(0,len(liste))
        y = random.randint(5,8)
        tab[liste[x][0]][liste[x][1]] = y
        return tab

    
    def __init__(self):

        tab1 = [[[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[3,0],[0,0]],
                [[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[2,0],[0,0]],
                [[1,0],[0,0],[4,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]]
        
        tab2 = [[[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
                [[0,0],[3,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[4,0],[0,0],[0,0],[0,0],[2,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0]],
                [[0,0],[0,0],[2,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[4,0],[0,0],[0,0]]]
        
        tab3 = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[4,0],[0,0],[0,0],[0,0],[3,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[2,0],[0,0]],
                [[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[3,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[4,0],[0,0]]]
                
        tab4 = [[[0,0],[0,0],[0,0],[0,0],[0,0],[4,0],[0,0],[0,0]],
                [[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[2,0],[0,0],[0,0],[0,0]],
                [[0,0],[3,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[4,0],[0,0]]]

        liste = [tab1,tab2,tab3,tab4]
        for i in range(len(liste)):
            nb_rotation = random.randint(0,3)
            liste[i] = turn_board(liste[i],nb_rotation)
        a=5
        b=5
        c=5
        d=5
        a = random.randint(0,3)
        while(b == a):
            b =random.randint(0,3)
        while(c == a or c == b):
            c =random.randint(0,3)
        while(d == a or d == b or d == c):
            d =random.randint(0,3)
        tab = assemble_pieces(liste[a],liste[b],liste[c],liste[d])
        tab = place_robot_random(tab)
        tab = change_target(tab)
        



    




