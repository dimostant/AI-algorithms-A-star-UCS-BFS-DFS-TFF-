#Create a class for Nodes
class Nodes():
    #Defining and Initializing variables
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    #Defining and Initializing position - returning its new variable
    def __eq__(self, other):
        return self.position == other.position

    def print(self):
        print(self.parent)
        print(self.position)
        print(self.g)
        print(self.h)
        print(self.f)


def Apathfinding(maze, start, end):  # maze is the tuples we will use for the algorithm

    #Create start and end Node as well as initialize their g,h and f costs
    start_Node = Nodes(None, start)
    start_Node.g = start_Node.h = start_Node.f = 0

    goal_Node = Nodes(None, end)
    goal_Node.g = goal_Node.h = goal_Node.f = 0

    #Initialize open and closed Lists
    open_List = []
    explored_nodes = []

    #Adding start_Node in the open_List
    open_List.append(start_Node)

    while len(open_List) > 0:  # Loop until end is found or open_List is empty

        #Get the current_Node and its Index
        current_Node = open_List[0]
        current_Index = 0

        # enumerate counts the items in open_list (i,item) with i >= 0
        for index, item in enumerate(open_List):
            print(index, item)
            if item.f < current_Node.f:
                current_Node = item
                current_Index = index

        open_List.pop(current_Index)  # We pop the item from open_List
        explored_nodes.append(current_Node)  # We add it in explored_nodes

        #If we find the goal_Node
        if current_Node == goal_Node:
            path = []
            current = current_Node  # We store the current_Node
            while current is not None:
                # We add the position to the list path
                path.append(current.position)
                current = current.parent  # We store the Parent Node

            # Trace back until the Beginning is reached
            return path[::-1],

        #Generate neighbours
        Neighbours = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            #Get the new position
            node_position = (
                current_Node.position[0] + new_position[0], current_Node.position[1] + new_position[1])

            #Make sure its within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            #Make sure the tarrain is walkable
            if maze[node_position[0]][node_position[1]] == '0':
                continue

            #Store the Node and its position
            new_Node = Nodes(current_Node, node_position)
            #Add the new_Node in the Neighbours list
            Neighbours.append(new_Node)

        #Loop through Neighbours
        for neighbour in Neighbours:
            #If neighbour is in explored_nodes then break the for loop
            check = False
            for explored_neighbour in explored_nodes:
                if neighbour == explored_neighbour:
                    check = True
                    continue
            #If check true, break the loop here
            if check:
                continue

            #If the position has g.Cost 1
            if maze[node_position[0]][node_position[1]] == '1':
                neighbour.g = current_Node.g + 1
                neighbour.h = ((neighbour.position[0] - goal_Node.position[0]) ** 2) + (
                    (neighbour.position[1] - goal_Node.position[1]) ** 2)
                neighbour.f = neighbour.g + neighbour.h

            #If the position has g.Cost 2
            if maze[node_position[0]][node_position[1]] == '2':
                neighbour.g = current_Node.g + 2
                neighbour.h = ((neighbour.position[0] - goal_Node.position[0]) ** 2) + (
                    (neighbour.position[1] - goal_Node.position[1]) ** 2)
                neighbour.f = neighbour.g + neighbour.h

            #if the neighbour is in the open_List
            check = False
            for open_Node in open_List:
                if neighbour == open_Node and neighbour.g > open_Node.g:
                    check = True
                    continue
            if check:
                continue

            #Add neighbour in the open_List
            open_List.append(neighbour)


def main():

    maze = [
            ['1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '1', '0'],  # row(0,12)
            ['1', '1', '1', '2', '0', '1', '1', '1','1', '1', '2', '1', '0'],  # row(1,12)
            ['0', '1', '0', '1', '1', '1', '1', '0','0', '1', '0', '1', '0'],  # row(2,12)
            ['1', '1', '2', '0', '1', '2', '0', '1','1', '2', '1', '1', '1'],  # row(3,12)
            ['0', '0', '1', '1', '0', '1', '1', '1','0', '0', '0', '0', '1'],  # row(4,12)
            ['1', '2', '1', '0', '1', '0', '1', '1','0', '0', '1', '1', '1'],  # row(5,12)
            ['0', '1', '2', '0', '1', '0', '0', '2','1', '1', '2', '0', '2'],  # row(6,12)
            ['1', '0', '1', '1', '2', '1', '1', '1', '0', '1', '1', '1', '1'],  # row(7,12)
            ['1', '1', '2', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1'],  # row(8,12)
            ['0', '0', '1', '1', '1', '1', '0', '1','1', '1', '1', '1', '2'],  # row(9,12)
            ['0', '0', '1', '0', '0', '1', '1', '2', '0', '0', '0', '1', '1'],  # row(10,12)
            ['0', '0', '0', '0', '0', '0', '0', '0','0', '0', '0', '0', '0']  # row(11,12)
           ]

    start = (9, 2)
    end = (10, 12)

    path = Apathfinding(maze, start, end)
    print('The path is:', path)


if __name__ == '__main__':
    main()
