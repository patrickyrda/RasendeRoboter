from game.state import State
from copy import deepcopy

# TODO: SIMPLIFY THIS FUNCTION , MAYBE CHANAGE FROM SET TO LIST OR SOMETHING ELSE, 
def get_next_states(parent : State, heuristics_table : list[list[int]]) -> set[State]:
    
    next_states = set()
    # ROBOT DIDNT MOVE, COUNTER PRODUCTIVE MOVE, GOOD Move
    idx = 0
    for robot in parent.robots:
        # print("\nThe coords of the robot "+str(robot.color)+"are X: "+str(robot.x)+" Y: "+str(robot.y)+"\n")
        ogx, ogy = robot.x, robot.y
        x, y = robot.move_right(parent.board.board)

        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_right(new_state.robots[idx])
            # next_states.add((f"Right move by robot {robot.color} at ({ogx}, {ogy}) to ({x}, {y})", new_state))
            next_states.add(new_state)
        # else: 
            # print("Counter productive right move for robot "+str(robot.color)+" from x: "+str(robot.x)+" y: "+str(robot.y)+"to "+"newx: "+str(x)+" newy: "+str(y)+ "would be passing from "+str(heuristics_table[ogx][ogy])+" to "+str(heuristics_table[x][y]))
        
        ogx, ogy = robot.x, robot.y
        x, y = robot.move_left(parent.board.board)

        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_left(new_state.robots[idx])
            # next_states.add((f"Left move by robot {robot.color} at ({ogx}, {ogy}) to ({x}, {y})", new_state))
            next_states.add(new_state)

        # else: 
            # print("Counter productive left move for robot "+str(robot.color)+" from x: "+str(robot.x)+" y: "+str(robot.y)+"to "+"newx: "+str(x)+" newy: "+str(y)+ "would be passing from "+str(heuristics_table[ogx][ogy])+" to "+str(heuristics_table[x][y]))
        

        ogx, ogy = robot.x, robot.y
        x, y = robot.move_down(parent.board.board)

        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_down(new_state.robots[idx])
            # next_states.add((f"Down move by robot {robot.color} at ({ogx}, {ogy}) to ({x}, {y})", new_state))
            next_states.add(new_state)
        # else: 
            # print("Counter productive down move for robot "+str(robot.color)+" from x: "+str(robot.x)+" y: "+str(robot.y)+"to "+"newx: "+str(x)+" newy: "+str(y)+ "would be passing from "+str(heuristics_table[ogx][ogy])+" to "+str(heuristics_table[x][y]))


        ogx, ogy = robot.x, robot.y
        x, y = robot.move_up(parent.board.board)

        if heuristics_table[x][y] <= heuristics_table[ogx][ogy] and (x != ogx or y != ogy):
            new_state = deepcopy(parent)
            new_state.slide_robot_up(new_state.robots[idx])
            # next_states.add((f"Up move by robot {robot.color} at ({ogx}, {ogy}) to ({x}, {y})", new_state))
            next_states.add(new_state)
        # else: 
            # print("Counter productive up for robot "+str(robot.color)+" from x: "+str(robot.x)+" y: "+str(robot.y)+"to "+"newx: "+str(x)+" newy: "+str(y)+"would be passing from "+str(heuristics_table[ogx][ogy])+" to "+str(heuristics_table[x][y]))
        
        idx += 1
        
    return next_states

# TODO: PASS THIS INSIDE OF THE CLASS State DEFINITION    
def is_goal(state : State) -> bool:
    
    return (state.board.board[state.target[0]][state.target[1]].has_robot == state.target_color)