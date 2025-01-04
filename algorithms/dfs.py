from .helpers import get_next_states, is_goal
from game.state import State

def dfs(state: State) -> list[State]:
    """
    Implementation of the Depth First Search algorithm to solve the Rasende Roboter game.

    Parameters:
    state (State): The initial state of the game

    Returns:
    list[State]: The path from the initial state to the goal state
    """
    heuristics_table = state.board.heuristics_board(state.target[0], state.target[1])
    stack = [state]  # Use a list as a stack
    visited = set([state])
    parent_map = {state: None}

    while stack:
        current_state = stack.pop()  # Remove the last element (LIFO order)

        if is_goal(current_state):
            # Build the path from the initial state to the goal state
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = parent_map[current_state]
            path.reverse()
            return path

        for neighbor in get_next_states(current_state, heuristics_table):
            if neighbor not in visited:
                stack.append(neighbor)  # Push the neighbor onto the stack
                visited.add(neighbor)
                parent_map[neighbor] = current_state

    print("\nNothing returned")
    return None
