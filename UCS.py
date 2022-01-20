import sys

max_possible_value = sys.maxsize

def pop_frontier(frontier):
    #if there is no frontier, no element can be popped, return false
    if len(frontier) == 0:
        return None
    min = max_possible_value
    max_values = []
    #from every elemnt get cost and path, then keep paths with min cost
    for key, path in frontier:
        if key == min:
            max_values.append(path)
        elif key < min:
            min = key
            #if a path with smaller cost is found, recorded paths are expensive
            #hence they get pulled out from the list, allowing only minimum cost paths
            max_values.clear()
            max_values.append(path)

    #sort every path with order of sequence in path (0, 1, 2 ,3...etc)
    max_values = sorted(max_values, key=lambda x: x[-1])

    #return cost and path of first in sequence element
    #then since it will get used, remove it from frontier
    desired_value = max_values[0]
    frontier.remove((min, max_values[0]))
    return min, desired_value


def get_frontier_params_new(node, frontier):
    #compare every node in frontier with the given
    #if nothing found return false, else return
    #true, position, cost, path 
    for i in range(len(frontier)):
        curr_tuple = frontier[i]
        cost, path = curr_tuple
        if path[-1] == node:
            return True, i, cost, path

    return False, None, None, None


def uniform_cost_search(graph, start, goal, standard_cost, door_cost):    
    #initialize path result and explored nodes list 
    path = []    
    explored_nodes = list()    

    #return 0 if the goal is the first node 
    if start == goal:    
        return path, explored_nodes    
    
    #create start element and add it to frontier  
    path.append(start)  
    path_cost = 0    
    
    frontier = [(path_cost, path)]

    #begin expanding frontier nodes. If they' ve all been expanded and goal isnt returned, then there is no goal
    while len(frontier) > 0:
        #visit cheapest element of frontier (choice in pop_frontier)
        path_cost_till_now, path_till_now = pop_frontier(frontier)    
        current_node = path_till_now[-1] 
        explored_nodes.append(current_node)    
    
        #if visited node is goal return
        if current_node == goal:    
            return path_till_now, explored_nodes    

        #create a list with neighbour nodes
        neighbours = graph[current_node]  

        #create a cost list that will hold standard cost or extra cost depending on the node according to the node sequence
        neighbour_cost_list = []
        index = 0
        
        #if cost contains a character it has extra cost, X means can't visit or that the cost is infinite
        #Implemented with max_size from sys
        for neighbour in neighbours :
           if neighbour[-1].isalpha():
               #door
               if neighbour[-1] == 'D' :
                   neighbour_cost_list.append(door_cost)
                   neighbours[index] = neighbour[:-1]
               #deadlock
               elif neighbour[-1] == 'X' :
                   neighbour_cost_list.append(max_possible_value)
                   neighbours[index] = neighbour[:-1]
               #unknown element
               else :
                   print("Error In Graph")
                   return None, None
           else :
               #standard step
               neighbour_cost_list.append(standard_cost)
           index += 1

        #convert neighbours to int, sort altoghether with cost list, then converting ints to strings
        neighbours_list_int = [int(n) for n in neighbours]    
        neighbours_list_int, neighbour_cost_list = zip(*sorted(zip(neighbours_list_int, neighbour_cost_list)))   
        neighbours_list_str = [str(n) for n in neighbours_list_int] 

        #index of neighbour
        index = 0
        #check every neighbour and create their node form
        for neighbour in neighbours_list_str:  
            #creating new available path for neighbour
            path_to_neighbour = path_till_now.copy()    
            path_to_neighbour.append(neighbour)   

            #use extra cost from the list and add it to the already given cost
            extra_cost = neighbour_cost_list[index]   
            neighbour_cost = extra_cost + path_cost_till_now    
            #create node element
            new_element = (neighbour_cost, path_to_neighbour)    

            #check if it exists in frontier and get it first instance (cheapest paths and first one seen), then remove from frontier
            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(neighbour, frontier)    

            #if neighbour node isnt visited or in frontier then add to frontier , else if it is in frontier and the cost is
            if (neighbour not in explored_nodes) and not is_there:    
                frontier.append(new_element)    
            elif is_there:    
                if neighbour_old_cost > neighbour_cost:    
                    frontier.pop(indexx)
                    frontier.append(new_element) 
            index += 1
    #no goal found in frontier, return none
    return None, None  
