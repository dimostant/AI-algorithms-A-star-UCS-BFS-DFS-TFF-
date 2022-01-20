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

def get_frontier_params_new(node, frontier):
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None


def get_frontier_params(node, frontier):
    for i in range(len(frontier.queue)):
        curr_tuple = frontier.queue[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None


def Apathfinding(graph, start, end, standard_cost, door_cost):


    path = []
    explored_nodes = list()
    
    if start == end:
        return path, explored_nodes

    path.append(start)
    path_cost = get_manhattan_heuristic(start, end)
    frontier = [(path_cost, path)]
    while len(frontier) > 0:

        path_cost_till_now, path_till_now = pop_frontier(frontier)
        current_node = path_till_now[-1]

        path_cost_till_now = path_cost_till_now - \
            get_manhattan_heuristic(current_node, end)
        explored_nodes.append(current_node)

        if current_node == end:
            return path_till_now, explored_nodes

        neighbours = graph[current_node]
        neighbour_cost_list = []
        index = 0

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

        neighbours_list_int = [int(n) for n in neighbours]
        neighbours_list_int, neighbour_cost_list = zip(*sorted(zip(neighbours_list_int, neighbour_cost_list)))   
        neighbours_list_str = [str(n) for n in neighbours_list_int]
        index = 0
        for neighbour in neighbours_list_str:
            path_to_neighbour = path_till_now.copy()
            path_to_neighbour.append(neighbour)
            
            extra_cost = neighbour_cost_list[index]    
            neighbour_cost = extra_cost + path_cost_till_now + \
                get_manhattan_heuristic(neighbour, end)
            new_element = (neighbour_cost, path_to_neighbour)

            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(
                neighbour, frontier)

            if (neighbour not in explored_nodes) and not is_there:
                frontier.append(new_element)

            elif is_there:
                if neighbour_old_cost > neighbour_cost:
                    frontier.pop(indexx)
                    frontier.append(new_element)
        index += 1
    return None, None
