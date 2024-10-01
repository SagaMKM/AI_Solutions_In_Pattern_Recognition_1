import numpy as np
import copy
import constants as c
import logic
from multiprocessing.pool import ThreadPool

pool = ThreadPool(4)
transposition_table = {}


commands = {
    c.KEY_UP: logic.up,
    c.KEY_DOWN: logic.down,
    c.KEY_LEFT: logic.left,
    c.KEY_RIGHT: logic.right
}


def AI_play(matrix, max_depth):
    best_score = -1000000
    best_key = None
    
    
    for key in commands.keys():
        tmp_score = score_toplevel_move(key, matrix, max_depth)
        if tmp_score > best_score:
            best_score = tmp_score
            best_key = key

    return best_key


def score_toplevel_move(key, board, max_depth):
    """
    Entry point to score the first move.
    """
    newboard, done, points = commands[key](board)

   
    if not done:
        return -1000000

    if max_depth == -1:
        empty_tiles = sum(sum(np.array(newboard) == 0))
        if empty_tiles > 12:
            max_depth = 1
        elif empty_tiles > 7:
            max_depth = 2
        elif empty_tiles > 4:
            max_depth = 3
        elif empty_tiles >= 1:
            max_depth = 4
        else:
            max_depth = 6

    score = calculate_chance(newboard, 0, max_depth)
    return score

def calculate_chance(board, curr_depth, max_depth):
    if curr_depth >= max_depth:
        
        return heuristic_corner_max(board)

    possible_boards_2 = []
    possible_boards_4 = []

    for x in range(c.GRID_LEN):
        for y in range(c.GRID_LEN):
            if board[x][y] == 0:
                new_board_2 = copy.deepcopy(board)
                new_board_2[x][y] = 2
                possible_boards_2.append(new_board_2)

                new_board_4 = copy.deepcopy(board)
                new_board_4[x][y] = 4
                possible_boards_4.append(new_board_4)
#oma
    score_2 = np.mean([calculate_max(b, curr_depth + 1, max_depth) for b in possible_boards_2])
    score_4 = np.mean([calculate_max(b, curr_depth + 1, max_depth) for b in possible_boards_4])

    return 0.9 * score_2 + 0.1 * score_4  


def calculate_max(board, curr_depth, max_depth):
    if curr_depth >= max_depth:
        return heuristic_corner_max(board)

    best_score = 0
    
    #iterointi
    for key in commands.keys():
        successor, done, _ = commands[key](board)
        if not done:
            continue
        score = calculate_chance(successor, curr_depth + 1, max_depth)
        if best_score < score:
            best_score = score

    return best_score

def heuristic_corner_max(matrix):
    best_score = -1
    return_key = None
    #kulmat
    corners = [(0, 0), (0, c.GRID_LEN - 1), (c.GRID_LEN - 1, 0), (c.GRID_LEN - 1, c.GRID_LEN - 1)]
    
    #Isoin tile ja sen positio
    max_tile = -1
    max_pos = (-1, -1)
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN):
            if matrix[i][j] > max_tile:
                max_tile = matrix[i][j]
                max_pos = (i, j)


    max_in_corner = max_pos in corners

    #laskenta
    n_empty = sum(matrix[i][j] == 0 for i in range(c.GRID_LEN) for j in range(c.GRID_LEN))

    #prio empty tile ja isoin nurkassa
    score = (n_empty * 2) + (max_tile if max_in_corner else 0)

    return score
