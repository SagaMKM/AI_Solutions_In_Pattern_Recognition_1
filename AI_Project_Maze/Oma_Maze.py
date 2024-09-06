import heapq

class Node:
    """A node class for A* Pathfinding with direction handling"""
    def __init__(self, parent=None, position=None, direction=None):
        self.parent = parent
        self.position = position
        self.direction = direction
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"Node(pos={self.position}, dir={self.direction})"


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_names = ['Right', 'Down', 'Left', 'Up']

    #alku ja oikeasuunta
    start_node = Node(None, start, 3)  #alkaa, katsoen ylöspäin
    end_node = Node(None, end)

    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add((current_node.position, current_node.direction))
        #testaus print
        print(f"Processing Node: {current_node.position} facing {direction_names[current_node.direction]}")

        # Found the goal
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []

        #eteenpäin
        move_forward_position = (current_node.position[0] + directions[current_node.direction][0],
                                 current_node.position[1] + directions[current_node.direction][1])
        if (0 <= move_forward_position[0] < len(maze) and
            0 <= move_forward_position[1] < len(maze[0]) and
            maze[move_forward_position[0]][move_forward_position[1]] == 0):
            if (move_forward_position, current_node.direction) not in closed_list:
                new_node = Node(current_node, move_forward_position, current_node.direction)
                children.append(new_node)

        #oikeelle kääntyminen
        new_direction = (current_node.direction + 1) % 4
        turn_right_position = (current_node.position[0] + directions[new_direction][0],
                               current_node.position[1] + directions[new_direction][1])
        if (0 <= turn_right_position[0] < len(maze) and
            0 <= turn_right_position[1] < len(maze[0]) and
            maze[turn_right_position[0]][turn_right_position[1]] == 0):
            if (turn_right_position, new_direction) not in closed_list:
                new_node = Node(current_node, turn_right_position, new_direction)
                children.append(new_node)

        for child in children:
            if (child.position, child.direction) in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs(child.position[1] - end_node.position[1])
            child.f = child.g + child.h

            heapq.heappush(open_list, child)
            print(f"Added to open list: {child.position} facing {direction_names[child.direction]}")

    return None


def main():
    maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
             [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             [1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
             [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]]
#Row (ylhäältä alaspäin), Column (vasemmalta oikeelle)
    start1 = (11, 10)
    end1 = (11, 2)

    path = astar(maze1, start1, end1)
    print(f"Path: {path}")


if __name__ == '__main__':
    main()
