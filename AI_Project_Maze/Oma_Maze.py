class Node():
    """A node class for Pathfinding with right turn and straight constraints"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        

    def __eq__(self, other):
        return self.position == other.position


def turn_right(direction):
    """Turn right from the current direction"""
    # Directions: 0 = right, 1 = down, 2 = left, 3 = up
    return (direction + 1) % 4


def move_in_direction(position, direction):
    """Move one step in the given direction"""
    if direction == 0:  # Right
        return (position[0], position[1] + 1)
    elif direction == 1:  # Down
        return (position[0] + 1, position[1])
    elif direction == 2:  # Left
        return (position[0], position[1] - 1)
    elif direction == 3:  # Up
        return (position[0] - 1, position[1])


def is_within_bounds(maze, position):
    """Check if the position is within the maze boundaries"""
    return 0 <= position[0] < len(maze) and 0 <= position[1] < len(maze[0])


def solve_maze_with_turns(maze, start, end):
    """Solves the maze with the rule that you can only turn right or go straight"""

    # Directions: 0 = right, 1 = down, 2 = left, 3 = up
    current_position = start
    direction = 0  # Start by facing right
    path = [current_position]

    while current_position != end:
        # Try to move straight
        next_position = move_in_direction(current_position, direction)
        
        if is_within_bounds(maze, next_position) and maze[next_position[0]][next_position[1]] == 0:
            # Move straight if possible
            current_position = next_position
            path.append(current_position)
        else:
            # Turn right and try again
            direction = turn_right(direction)
    
    return path


def main():
    # The maze we are solving
    maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0 ,1, 1, 1, 0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0 ,1, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]

    start1 = (11, 10)
    end1 = (11, 2)

    path = solve_maze_with_turns(maze1, start1, end1)
    print("Path to the solution:", path)


if __name__ == '__main__':
    main()
