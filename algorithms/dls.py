from collections import deque
from .helpers import get_next_states, is_goal
from game.state import State

def dfs(state: State, visited=None) -> list[State] | None:
    if visited is None:
        visited = set()
    visited.add(state)
    
    if is_goal(state):
        return [state]

    heur = state.board.heuristics_board_new(state.target[0], state.target[1])

    for next_state in get_next_states(state, heur):
        if next_state not in visited:
            path = dfs(next_state, visited)
            if path: 
                return [state] + path

    return None

def dls(state: State, visited=None, depth=0, max_depth=10) -> list[State] | None:
    
    """
    Performs a Depth-Limited Search (DLS) to find a path to the goal state within a specified depth limit.

    Parameters:
    state (State): The current state of the game board.
    visited (set, optional): A set of visited states to avoid revisiting. Defaults to None, which initializes an empty set.
    depth (int, optional): The current depth level in the search. Defaults to 0, since we always start from the beginning state.
    max_depth (int, optional): The maximum depth allowed for the search. Defaults to 10.

    Returns:
    list[State] | None: A list of states representing the path to the goal state if found within the depth limit, 
                         otherwise None if the goal is not reachable within the limit.
    """

    if visited is None:
        visited = set()

    visited.add(state)

    if is_goal(state):
        return [state]

    if depth >= max_depth:
        print(f"Max depth {max_depth} reached, stopping recursion.")
        return None

    heur = state.board.heuristics_board_new(state.target[0], state.target[1])
    
    for next_state in get_next_states(state, heur):
        if next_state not in visited:
            path = dls(next_state, visited, depth + 1, max_depth)
            if path:
                return [state] + path

    return None