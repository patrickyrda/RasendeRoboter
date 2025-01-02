from collections import deque
from .helpers import get_next_states, is_goal
from game.state import State

# Normally it will be used for the normal level , MAYYBE THATS A GREEDY BFS SINCE IT USES AN HEURISTIC FUNCTION 
def bfs(state : State) -> list[State]:
    """
    Implementation of the "Greedy" Breadth First Search algorithm to solve the Rasende Roboter game.
    
    Parameters:
    state (State): The initial state of the game
    
    Returns:
    list[State]: The path from the initial state to the goal state
    """
    # TODO: THE NEW HEURISTICS BOARD WORKS BETTER REDUCING THE TIME OF EXECUTION, BUT THE __eq__ and OTHERS WORK BETTER FOR OLD VERSION 
    heuristics_table = state.board.heuristics_board_new(state.target[0], state.target[1])
    queue = deque([state])
    visited = set([state])
    parent_map = {
        state: None
        }

    while queue:
        current_state = queue.popleft()

        if is_goal(current_state):
            path = []
            while current_state != None:
                path.append(current_state)
                current_state = parent_map[current_state]
            path.reverse()
            return path
        heuristics_table = current_state.board.heuristics_board_new(current_state.target[0], current_state.target[1])

        for neighboor in get_next_states(current_state, heuristics_table):
            if neighboor not in visited:
                queue.append(neighboor)
                visited.add(neighboor)
                parent_map[neighboor] = current_state
            
    print("\nNothing returned")
    return None
    

