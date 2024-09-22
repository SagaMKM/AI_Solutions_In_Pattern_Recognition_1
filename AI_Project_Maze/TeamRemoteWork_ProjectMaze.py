# -*- coding: utf-8 -*-
"""
 
This code is from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
Except the Maze is now for the Labyrinth task for Tekniska Museet case
 
"""
class Node():
    """A node class for A* Pathfinding"""
    #Node on kaytannossa ruutu ruudukossa jolle tehdaan tai on tehtu laskelmia
    #Tama on konstruktori jossa objektille annetaan "vanhempi". Vanhempi pitaa tietaa jotta voidaan "backtrackata"
    #loydetty reitti takaisin ja saadaan se listaan. Positio kertoo taman kyseisen noden paikan ruudukossa: x, y.
    #
    def __init__(self, parent=None, position=None, direction = None):
        self.parent = parent
        self.position = position
        self.direction = direction
 
        self.g = 0  # taman noden etaisyys aloitus nodeen
        self.h = 0  # taman noden etaisyys maaranpaahan
        self.f = 0 # Tarkoitus valita matalin F kustannus aina.
 
    def __eq__(self, other):    #Tama on automaattisesti suoritettava funtio joka kysyy onkoa oma positio sama kuin toinen positio
        return self.position == other.position
 
 
def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    # Create start and end node
    #Luodaan alku ja loppu node ja asetetaan niiden g, h ja f arvot nollaan
    start_node = Node(None, start, "up")
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0
    # Initialize both open and closed list
    #Kaytetaan avointa listaa ja suljettua listaa niin etta tiedetaan mita nodeja voidaan "prosessoida" ja mitka on jo prosessoitu.
    open_list = []
    closed_list = []
 
    # Add the start node
    #Lisataan aloitusnode avoimeen listaan
    open_list.append(start_node)
    # Loop until you find the end
    #Niin kauan kuin avoimessa listassa on jotain prosessoitavaa, prosessoidaan
    while len(open_list) > 0:
        print("***")
        # Get the current node
        #Otetaan tuolta open listista node prosessoitavaksi, joka on listan ensimmainen node.
        current_node = open_list[0]
        current_index = 0
            #Jos open listassa olevista nodeista jonkun f-kustannus on pienempi kuin talla hetkella kaytossa olevan noden,
            #vaihdetaan se "current nodeksi".
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
##
        # Pop current off open list, add to closed list
        #Otetaan se node jonka kustannus oli korkeampi ja poistetaan se open_listasta ja lisataan suljettuun listaan
 
        # if current_node.x > direction_Node.x:
        #     direction = "right"
        # elif current_node.x < direction_Node.x:
        #     direction = "left"
        # elif current_node.y < direction_Node.y:
        #     direction = "down"
        # else:
        #     direction = "up"
 
        open_list.pop(current_index)
        # closed_list.append(current_node)
        print(current_node.direction)
        print("Y: " + str(current_node.position[0]) + " X: " + str(current_node.position[1]))
        # Found the goal
        #Jos tamanhetkinen node on loppunode, luo lista "path", laita current node "currentiksi", sitten laitetaan tuo "current" siihen "path listaa"
        #ja sen jalkeen "currentiksi" taman hetkinen "currentin" parentti ja jatketaan kunnes kaikki nodet on kayty lavitse ja paastaan alku nodeen
        #Sitten otetaan se lista joka tuossa luotiin ja palautetaan se vaarinpain.
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path
 
        # Generate children
        children = []
 
        ##############################
        if current_node.direction == "up":
            # print("Original direction is UP")
            for new_position in [(-1, 0), (0, 1)]: # Adjacent squares
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue
 
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
 
                if current_node.position[0] > node_position[0]:
                    direction = "up"
                elif current_node.position[0] < node_position[0]:
                    direction = "down"
                elif current_node.position[1] < node_position[1]:
                    direction = "right"
                elif current_node.position[1] > node_position[1]:
                    direction = "left"
 
                new_node = Node(current_node, node_position, direction)
                print("Original Y" + str(current_node.position[0]) + " X" + str(current_node.position[1]))
                print("New Y" + str(node_position[0]) + "  X" + str(node_position[1]))
                print(new_node.direction)
 
                children.append(new_node)
 
        ###############################
 
        if current_node.direction == "down":
            # print("Original direction is DOWN")
            for new_position in [(1, 0), (0, -1)]: # Adjacent squares
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue
 
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
 
                if current_node.position[0] > node_position[0]:
                    direction = "up"
                elif current_node.position[0] < node_position[0]:
                    direction = "down"
                elif current_node.position[1] < node_position[1]:
                    direction = "right"
                elif current_node.position[1] > node_position[1]:
                    direction = "left"
 
                new_node = Node(current_node, node_position, direction)
                print("Original Y" + str(current_node.position[0]) + " X" + str(current_node.position[1]))
                print("New Y" + str(node_position[0]) + "  X" + str(node_position[1]))
                print(new_node.direction)
 
                children.append(new_node)
 
        ###############################
 
            
        if current_node.direction == "right":
            # print("Original direction is RIGHT")
            for new_position in [(0, 1), (1, 0)]: # Adjacent squares
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue
 
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
 
                if current_node.position[0] > node_position[0]:
                    direction = "up"
                elif current_node.position[0] < node_position[0]:
                    direction = "down"
                elif current_node.position[1] < node_position[1]:
                    direction = "right"
                elif current_node.position[1] > node_position[1]:
                    direction = "left"
 
                new_node = Node(current_node, node_position, direction)
                print("Original Y" + str(current_node.position[0]) + " X" + str(current_node.position[1]))
                print("New Y" + str(node_position[0]) + "  X" + str(node_position[1]))
                print(new_node.direction)
 
                children.append(new_node)
 
        ###############################
 
        if current_node.direction == "left":
            # print("Original direction is LEFT")
            for new_position in [(0, -1), (-1, 0)]: # Adjacent squares
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
                
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue
 
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
 
                if current_node.position[0] > node_position[0]:
                    direction = "up"
                elif current_node.position[0] < node_position[0]:
                    direction = "down"
                elif current_node.position[1] < node_position[1]:
                    direction = "right"
                elif current_node.position[1] > node_position[1]:
                    direction = "left"
 
                new_node = Node(current_node, node_position, direction)
                print("Original Y" + str(current_node.position[0]) + " X" + str(current_node.position[1]))
                print("New Y" + str(node_position[0]) + "  X" + str(node_position[1]))
                print(new_node.direction)
 
                children.append(new_node)
 
        ###############################
 
 
        # print(new_node.direction)
        # Loop through children
        for child in children:
            
            # Child is on the visited list (search entire visited list)
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue
 
            # Create the f, g, and h values
            child.g = current_node.g + 1
            ## Heuristic costs calculated here, this is using eucledian distance
            child.h = (((child.position[0] - end_node.position[0]) ** 2) +
                       ((child.position[1] - end_node.position[1]) ** 2))
 
            child.f = child.g + child.h
 
            # Child is already in the yet_to_visit list and f cost is already lower
            if len([open_node for open_node in open_list if child == open_node and child.f > open_node.f]) > 0:
                continue
 
            # Add the child to the yet_to_visit list
            open_list.append(child)
 
 
def main():
 
    # The maze we are actually looking for the solution
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
 
# Bit smaller maze but this one shows what can happen with the first move... Basically you could go to left or right first!
    # maze2 = [[0, 0, 0, 0, 0, 0],
    #          [0, 1, 0, 0, 1, 0],
    #          [0, 0, 0, 1, 0, 0]]
 
    # start2 = (2, 1)
    # end2 = (2, 4)
 
     # You could also test with this maze in the beginning and observe how the algorithms is working.
    # Note, that here also, the first move can be taken to ANY (basically to right or left)
    #maze3 = [[0, 0, 0],
    #        [0, 1, 0],
    #        [0, 0, 0]]
 
    # start3 = (2, 1)
    # end3 = (0, 2)
 
    path = astar(maze1, start1, end1)
    for x in path:
        print(x)
    # print(path)
 
 
if __name__ == '__main__':
    main()