from game.state import State
from copy import deepcopy

def get_next_states(parent : State, heuristics_table : list[list[int]]) -> set[State]:
    """
    Generates the next possible states from the given parent state by attempting to move each robot
    in all four directions (right, left, down, up) if the move is not counterproductive based on the 
    provided heuristics table.

    Parameters:
    parent (State): The current state of the board with robots.
    heuristics_table (list[list[int]]): A 2D list representing heuristic values for each board position,
                                        used to determine the desirability of moves.

    Returns:
    set[State]: A set of new states generated after moving the robots, excluding counterproductive moves.
    """
    next_states = set()
    idx = 0
    for robot in parent.robots:
        ogx, ogy = robot.x, robot.y
        x, y = robot.move_right(parent.board.board)
        # Right movement
        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_right(new_state.robots[idx])
            next_states.add(new_state)
        
        ogx, ogy = robot.x, robot.y
        x, y = robot.move_left(parent.board.board)
        # Left movement
        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_left(new_state.robots[idx])
            next_states.add(new_state)


        ogx, ogy = robot.x, robot.y
        x, y = robot.move_down(parent.board.board)
        # Down movement
        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_down(new_state.robots[idx])
            next_states.add(new_state)

        ogx, ogy = robot.x, robot.y
        x, y = robot.move_up(parent.board.board)
        # Up movement
        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_up(new_state.robots[idx])
            next_states.add(new_state)
        
        idx += 1
        
    return next_states

def is_goal(state : State) -> bool:
    """
    Checks if the given state is the goal state by comparing the robot at the target position
    with the target color.

    Parameters:
    state (State): The state to be checked.

    Returns:
    bool: True if the state is the goal state, False otherwise.
    """
    return (state.board.board[state.target[0]][state.target[1]].has_robot == state.target_color)




def get_next_states_new(parent : State) -> set[State]:
    
    """
    Generates all possible next states by moving each robot in all four directions. It also generates counter-productive moves

    Parameters:
    parent (State): The state from which to generate the next states.

    Returns:
    set[State]: A set of new states generated after moving the robots in all four directions.
    """
    next_states = set()
    idx = 0
    for robot in parent.robots:

        
        new_state = deepcopy(parent)
        new_state.slide_robot_right(new_state.robots[idx])
        next_states.add(new_state)
        

        new_state = deepcopy(parent)
        new_state.slide_robot_left(new_state.robots[idx])
        next_states.add(new_state)


        new_state = deepcopy(parent)
        new_state.slide_robot_down(new_state.robots[idx])
        next_states.add(new_state)


        new_state = deepcopy(parent)
        new_state.slide_robot_up(new_state.robots[idx])
        next_states.add(new_state)
        
        idx += 1
        
    return next_states




