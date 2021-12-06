import sys

max_possible_value = sys.maxsize

def pop_frontier(frontier):
    if len(frontier) == 0:
        return None
    # copied_list = frontier.copy()
    min = max_possible_value
    max_values = []
    for key, path in frontier:
        if key == min:
            max_values.append(path)
        elif key < min:
            min = key
            max_values.clear()
            max_values.append(path)

    max_values = sorted(max_values, key=lambda x: x[-1])
    # max_values.sort()
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


#custom implementations, test to see if they are accurate ~ for Dimos
# def pop_frontier(frontier):
#     return frontier[0][0], frontier[0][1]

# def get_frontier_params_new(neighbour, frontier):
#     print("\n \n \n" , neighbour, frontier)
#     is_there = False
#     for _ in frontier :
#         if neighbour == _ : 
#             is_there = True

#     if is_there == False :
#         indexx = None 
#         neighbour_old_cost = 0

#     #Calculate cost if neighbour exists 
    
#   return  is_there, indexx, neighbour_old_cost
