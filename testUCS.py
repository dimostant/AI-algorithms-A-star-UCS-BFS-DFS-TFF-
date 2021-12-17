from foreignBasicFunctions import pop_frontier, get_frontier_params_new

def uniform_cost_search(graph, start, goal, standard_cost, door_cost):    
    path = []    
    explored_nodes = list()    

    if start == goal:    
        return path, explored_nodes    
    
    path.append(start)  
    path_cost = 0    
    
    frontier = [(path_cost, path)]

    while len(frontier) > 0:

        path_cost_till_now, path_till_now = pop_frontier(frontier)    
        current_node = path_till_now[-1] 
        explored_nodes.append(current_node)    
    
        if current_node == goal:    
            return path_till_now, explored_nodes    
    

        neighbours = graph[current_node]  
    
        neighbour_cost_list = []
        index = 0
        
        for neighbour in neighbours :
           if neighbour[-1].isalpha():
               if neighbour[-1] == 'D' :
                   neighbour_cost_list.append(door_cost)
                   neighbours[index] = neighbour[:-1]
           else :
               neighbour_cost_list.append(standard_cost)
           index += 1

        neighbours_list_int = [int(n) for n in neighbours]   
        #neighbours_list_int.sort(reverse=False)   
        neighbours_list_int, neighbour_cost_list = zip(*sorted(zip(neighbours_list_int, neighbour_cost_list)))   
        neighbours_list_str = [str(n) for n in neighbours_list_int] 

        index = 0
        for neighbour in neighbours_list_str:    
            path_to_neighbour = path_till_now.copy()    
            path_to_neighbour.append(neighbour)   

            #extra_cost = 1
            extra_cost =  neighbour_cost_list[index]   
            neighbour_cost = extra_cost + path_cost_till_now    
            new_element = (neighbour_cost, path_to_neighbour)    
    
            is_there, indexx, neighbour_old_cost, _ = get_frontier_params_new(neighbour, frontier)    
    
            if (neighbour not in explored_nodes) and not is_there:    
                frontier.append(new_element)    
            elif is_there:    
                if neighbour_old_cost > neighbour_cost:    
                    frontier.pop(indexx)    
                    frontier.append(new_element) 
            index += 1           
    
    return None, None  
