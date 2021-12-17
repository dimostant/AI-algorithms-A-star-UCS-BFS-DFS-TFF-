# Using a Python dictionary to act as an adjacency list
from originalGraph import graph_neighbours



# DFS algorithm in Python

def DFS(adj_list, start, target, path, depth,max_depth,visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for neighbour in adj_list[start]:
        if neighbour not in visited:
            result = DFS(adj_list, neighbour, target, path,depth,max_depth, visited)
            if result is not None:
                return result
    path.pop()
    return None

# IDS algorithm in Python

def IDS(adj_list, start, target, path, visited = set()):

    current_depth=1
    bot_reach=False #Variable ama ftasame ston pato tou dentrou

    while not bot_reach:
        bot_reach= DFS(adj_list,start, target,path,0,current_depth,visited=set())
        if bot_reach is not None:
            return bot_reach

        current_depth=current_depth+1
        print("Increasing depth to " + str(current_depth))
        

    return None

traversal_path = []
traversal_path = IDS(graph_neighbours, '0','92',traversal_path)
print(traversal_path)