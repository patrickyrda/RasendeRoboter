# HAVE TO ADD VALUE FOR THE 17 Targets
def translate(value):
    '''
    Translate integer values represented in the board to their corresponding representation

    argument: integer value

    return: string representation
    '''
    translation_map = {
        1: "Green robot",
        2: "Red robot",
        3: "Blue robot",
        4: "Yellow robot",
        5: "Top barrier",
        6: "Down barrier",
        7: "Left barrier",
        8: "Right barrier",
        9: "Colored barrier",
        10: "Blocked center"
    }
    
    return translation_map.get(value, "Unknown value")