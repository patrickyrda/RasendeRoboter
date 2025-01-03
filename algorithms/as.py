from game.state import State
from collections import deque 
from sortedcontainers import SortedList
from .helpers import get_next_states, is_goal
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



"""
def As(state : State) -> list[State]:
    # This first try uses next states already eliminating counter productive moves and heuristics table is not update, may change that later as i think it will improve code
    
    
    Implements the A* algorithm to solve the Rasende Roboter game.
    
    Parameters:
    state (State): The initial state of the game
    
    Returns:
    list[State]: The path from the initial state to the goal state
    
    ClosedList = set()

    h_tt = state.board.heuristics_board_new(state.target[0], state.target[1])
    coord = state.get_robot_coords(target_robot=True)
    val_h = h_tt[coord[0]][coord[1]]
    state.set_as(0, val_h, None)
    OpenList = SortedList([state])
    count = 0
    while OpenList :
        # TODO: Here store by DESC order so i pop last with less O time
        count += 1
        current = OpenList.pop(0)

        print("\nThis is the Current state number : ", count)
        current.board.print_board()
        print("\n")

        if is_goal(current):
            return return_path(current)
        
        ClosedList.add(current)
        heuristics_table = state.board.heuristics_board_new(current.target[0], current.target[1])
        next = get_next_states(current, heuristics_table)
        print("\nHere is the next states of round : ", count)
        
        countt  = 0

        for neighboor in next:
            countt += 1
            # print("\nThis is next state number : ", countt)
            # print(neighboor.board.print_board())
            if neighboor in ClosedList:
                print("\nAlready in closed list")
                continue
            
            h_t = neighboor.board.heuristics_board_new(neighboor.target[0], neighboor.target[1])
            coords = neighboor.get_robot_coords(target_robot=True)
            # print("coords are: ", coords)
            heuristic = h_t[coords[0]][coords[1]]
            tentative_g = current.g + 1
            neighboor.set_as(tentative_g, heuristic, current)
            
            
            if neighboor not in OpenList:
                OpenList.add(neighboor)
            elif tentative_g >= neighboor.g:
                continue
            
            
            # print("\n")
            # print(h_t)
            # print("\n")
            
            # print("\n")
            # neighboor.board.print_board()
            
            

            
            # print("\n")
            # print("\nheuristic is : ", heuristic)
            # print("\n f is : ", neighboor.f)
            # print("\ng is : ", neighboor.g)
        print("\nHERE ARE THE OPENLIST AFTER ROUND ", count)
        print(" ".join(str(node.f) for node in OpenList))
    for node in OpenList:
        print("\n F is : ", node.f)
    for node in ClosedList:
        print("\n F Closoed is : ", node.f)
    return None

"""



    
    
