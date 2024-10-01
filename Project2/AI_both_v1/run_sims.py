import logic

def run_simulation(ai_function, runs=100):
    total_score = 0
    max_tile_reached = 0
    
    for _ in range(runs):
        matrix = logic.new_game(c.GRID_LEN)
        done = False
        while not done:
            matrix, done, _ = logic.add_two(matrix)
            move = ai_function(matrix, depth=-1)  # Use -1 for adaptive depth control
            matrix, done, _ = commands[move](matrix)
            
        score = np.max(matrix)
        total_score += score
        max_tile_reached = max(max_tile_reached, score)

    avg_score = total_score / runs
    print(f"Average Score: {avg_score}")
    print(f"Max Tile Reached: {max_tile_reached}")

# Running the simulation
run_simulation(AI_play, 100)
