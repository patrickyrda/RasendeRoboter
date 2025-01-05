from game.state import State
import time
from collections import deque 
from sortedcontainers import SortedList
from .helpers import get_next_states, is_goal
from typing import Union
# TODO: HEURISTICS TABLE HAS TO CHANGE VALUES WHEN ROBOT MOVES
def return_path(state : State) -> list[State]:
    """
    Rebuilds the path from the final state to the root of the state tree.
    
    Parameters:
    state (State): The state from which to start the path.
    
    Returns:
    list[State]: A list of states from the final state up to the root.
    """
    path = []
    current = state
    while current != None:
        path.insert(0, current)
        current = current.parent
    return path

# Slower than greedy BFS probably becaus eof the heuristics determination method 
def As(state: State) -> list[State]:
    """
    Implements the A* algorithm to solve the Rasende Roboter game.
    
    Parameters:
    state (State): The initial state of the game
    
    Returns:
    list[State]: The path from the initial state to the goal state
    """
    ClosedList = set()
    heur_ini = state.board.heuristics_board_new(state.target[0], state.target[1])
    x,y = state.get_robot_coords(target_robot=True)
    val_h = heur_ini[x][y]
    state.set_as(0, val_h, None)
    OpenList = SortedList([state])
    gcount = 0
    while OpenList:
        gcount += 1
        current = OpenList.pop(0)
        ClosedList.add(current)
        if is_goal(current):
            return return_path(current)
        
        heuristics_table_current = current.board.heuristics_board_new(current.target[0], current.target[1])

        for neighboor in get_next_states(current, heuristics_table_current):

            if neighboor not in ClosedList and neighboor not in OpenList or neighboor.g > current.g + 1:
                heur_table_neighboor = neighboor.board.heuristics_board_new(neighboor.target[0], neighboor.target[1])
                xn, yn = neighboor.get_robot_coords(target_robot=True)
                heuristic_value = heur_table_neighboor[xn][yn]
                neighboor.set_as(current.g + 1, heuristic_value, current)
                OpenList.add(neighboor)
        print("\nHERE ARE THE OPENLIST AFTER ROUND ", gcount)
        print(" ".join(str(node.f) for node in OpenList))  
    return None

def As_intorlist(state: State) -> Union[int, list[State]]:
    """
    Implements the A* algorithm to solve the Rasende Roboter game.
    
    Parameters:
    state (State): The initial state of the game
    
    Returns:
    list[State]: The path from the initial state to the goal state, or an integer if the time limit is exceeded
    or
    int: The 'f' value of the first node in OpenList after 80 seconds have elapsed
    """
    ClosedList = set()
    heur_ini = state.board.heuristics_board_new(state.target[0], state.target[1])
    x, y = state.get_robot_coords(target_robot=True)
    val_h = heur_ini[x][y]
    state.set_as(0, val_h, None)
    OpenList = SortedList([state])
    gcount = 0

    start_time = time.time()

    while OpenList:
        gcount += 1
        current = OpenList.pop(0)
        ClosedList.add(current)

        elapsed_time = time.time() - start_time
        if elapsed_time > 80: 
            if OpenList:
                return int(OpenList[0].f)
            else:
                return None 

        if is_goal(current):
            return return_path(current)
        
        heuristics_table_current = current.board.heuristics_board_new(current.target[0], current.target[1])

        for neighboor in get_next_states(current, heuristics_table_current):
            if neighboor not in ClosedList and (neighboor not in OpenList or neighboor.g > current.g + 1):
                heur_table_neighboor = neighboor.board.heuristics_board_new(neighboor.target[0], neighboor.target[1])
                xn, yn = neighboor.get_robot_coords(target_robot=True)
                heuristic_value = heur_table_neighboor[xn][yn]
                neighboor.set_as(current.g + 1, heuristic_value, current)
                OpenList.add(neighboor)


    return None



    
    
