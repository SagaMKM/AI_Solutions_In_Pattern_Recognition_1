import constants as c
import random
import logic

commands = {c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right}

def AI_play(matrix):
   
    #key = heuristic_random()
    #key = heuristic_empty_tile(matrix)
    key = heuristic_corner_max(matrix)  # Use the new heuristic here
    return key


def heuristic_corner_max(matrix):
    best_score = -1
    return_key = None
    
    # Coordinates for the four corners
    corners = [(0, 0), (0, c.GRID_LEN-1), (c.GRID_LEN-1, 0), (c.GRID_LEN-1, c.GRID_LEN-1)]
    
    # Find the current highest tile and its position
    max_tile = -1
    max_pos = (-1, -1)
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN):
            if matrix[i][j] > max_tile:
                max_tile = matrix[i][j]
                max_pos = (i, j)
    
    # Loop through all possible moves
    for key in commands.keys():
        game, done, points = commands[key](matrix)  

        if not done:
            continue

        # Heuristic: Check if the max tile remains in a corner
        n_empty = 0
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                if game[i][j] == 0:
                    n_empty += 1
        
        # Check if the max tile is in a corner after the move
        max_in_corner = max_pos in corners

        # Prioritize moves that keep the max tile in a corner and maximize empty spaces
        score = (n_empty * 2) + (max_tile if max_in_corner else 0)
        
        if score > best_score:
            best_score = score
            return_key = key

    print("Best move with Corner Max Heuristic: ", return_key)
    return return_key


def heuristic_random():
    tmp = [c.KEY_UP, c.KEY_DOWN, c.KEY_RIGHT, c.KEY_LEFT] 
    key=tmp[random.randint(0,3)]
    return key

def heuristic_empty_tile(matrix):
    best_score = -1
    return_key = None
    for key in commands.keys():
        game, done, points = commands[key](matrix)  

        if not done:
           pass

        if done:
            n_empty=0
            for i in range(c.GRID_LEN):
                for j in range(c.GRID_LEN):
                    if game[i][j]==0:
                        n_empty+=1
            if n_empty > best_score:
                best_score = n_empty
                return_key = key
           

    print("Best move seems to be: ")
    print(return_key)    

    return return_key

