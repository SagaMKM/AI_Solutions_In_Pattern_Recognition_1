import numpy as np
import constants as c
import random
import logic

commands = {c.KEY_UP: logic.up,
            c.KEY_DOWN: logic.down,
            c.KEY_LEFT: logic.left,
            c.KEY_RIGHT: logic.right}

# Note! depth has no effect for pure heuristic version!!
def AI_play(matrix, depth):
   
    #key = heuristic_random()
    
    key = heuristic_corner_max(matrix) 
    return key


def heuristic_corner_max(matrix):
    best_score = -1
    return_key = None
    
    corners = [(0, 0), (0, c.GRID_LEN-1), (c.GRID_LEN-1, 0), (c.GRID_LEN-1, c.GRID_LEN-1)]
    #suurin tile ja positio
    max_tile = -1
    max_pos = (-1, -1)
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN):
            if matrix[i][j] > max_tile:
                max_tile = matrix[i][j]
                max_pos = (i, j)
    

    for key in commands.keys():
        game, done, points = commands[key](matrix)  

        if not done:
            continue

        #tarkistaa onko suurin laatta kulmassa
        n_empty = 0
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                if game[i][j] == 0:
                    n_empty += 1
        
        #sama siirroon jälkeen
        max_in_corner = max_pos in corners

        #priorisoi liikkeitä mitkä pitää suurimman ruudun nurkassa
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
            n_empty=n_empty_tiles(game)
            if n_empty > best_score:
                best_score = n_empty
                return_key = key

    return return_key

def n_empty_tiles(matrix):       
    return sum(sum(np.array(matrix)==0))
