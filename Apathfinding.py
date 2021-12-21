import sys
max_possible_value = sys.maxsize

#create the manhatan adjacent list and all its requirements
def get_manhattan_heuristic(node, end):
    i, j = divmod(int(node), 8)
    i_end, j_end = divmod(int(end), 8)
    i_delta = abs(i - i_end)
    j_delta = abs(j - j_end)

    manhattan_dist = i_delta + j_delta
    return manhattan_dist


def pop_frontier(frontier):
    #if frontier has nothing, then return false
    if len(frontier) == 0:
        return None
    min = max_possible_value
    max_values = []
    #Loop, find and store all costs and paths until you find the path with the littlest cost
    for key, path in frontier:
        if key == min:
            max_values.append(path)
        elif key < min:
            min = key
            max_values.clear()
            max_values.append(path)
    #sorting in order
    max_values = sorted(max_values, key=lambda x: x[-1])
    #return the cost and the path of the first elements and remove it once used
    desired_value = max_values[0]
    frontier.remove((min, max_values[0]))
    return min, desired_value

#compare each new node with the given one and if something is found, return true
#with position,cost and path
#else, false!
def get_frontier_params_new(node, frontier):
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None

#compare each node with the given one and if something is found, return true
#with position,cost and path
#else, false!
def get_frontier_params(node, frontier):
    for i in range(len(frontier.queue)):
        curr_tuple = frontier.queue[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None


def Apathfinding(graph, start, end, standard_cost, door_cost):

#Initialize the path and expolred_nodes list
    path = []
    explored_nodes = list()
    #if start is also the end return 0
    if start == end:
        return path, explored_nodes

    #put start in path 
    path.append(start)
    path_cost = get_manhattan_heuristic(start, end)
    frontier = [(path_cost, path)]
    #after frontier is intialized start loop until end is found or until it's empty
    while len(frontier) > 0:

        #with the help of pop_frontier, find the cheapest 
        path_cost_till_now, path_till_now = pop_frontier(frontier)
        current_node = path_till_now[-1]

        #get the f cost of the node
        path_cost_till_now = path_cost_till_now - get_manhattan_heuristic(current_node, end)
        explored_nodes.append(current_node)

        #if the goal is found, return the path
        if current_node == end:
            return path_till_now, explored_nodes

        #create a lost of neighbours, cost_list and index to get the cost
        neighbours = graph[current_node]
        neighbour_cost_list = []
        index = 0

        #if cost contains a character it has extra cost, X means can't visit or that the cost is infinite
        #Implemented with max_size from sys
        for neighbour in neighbours:
           if neighbour[-1].isalpha():
               #door
               if neighbour[-1] == 'D':
                   neighbour_cost_list.append(door_cost)
                   neighbours[index] = neighbour[:-1]
               #deadlock
               elif neighbour[-1] == 'X':
                   neighbour_cost_list.append(max_possible_value)
                   neighbours[index] = neighbour[:-1]
               #unknown element
               else:
                   print("Error In Graph")
                   return None, None
           else:
               #standard step
               neighbour_cost_list.append(standard_cost)
           index += 1
          #convert neighbours to int, sort altoghether with cost list, then converting ints to strings
        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int.sort(reverse=False)
        neighbours_list_str = [str(n) for n in neighbours_list_int]

        for neighbour in neighbours_list_str:
            #creating new available path for neighbour
            path_to_neighbour = path_till_now.copy()
            path_to_neighbour.append(neighbour)

            #use extra cost from the list and add it to the already given cost
            extra_cost = 1

            neighbour_cost = extra_cost + path_cost_till_now +  get_manhattan_heuristic(neighbour, end)
            new_element = (neighbour_cost, path_to_neighbour)

            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(
                neighbour, frontier)

            if (neighbour not in explored_nodes) and not is_there:
                frontier.append(new_element)

            elif is_there:
                if neighbour_old_cost > neighbour_cost:
                    frontier.pop(indexx)
                    frontier.append(new_element)

    return None, None
