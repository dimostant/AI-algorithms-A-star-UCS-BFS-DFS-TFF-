# Using a Python dictionary to act as an adjacency list

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


def IDS(adj_list, start, target, path, visited = set()):

    current_depth=1
    #if tree depth is reached
    bot_reach=False

    while not bot_reach:
        bot_reach= DFS(adj_list,start, target,path,0,current_depth,visited=set())
        if bot_reach is not None:
            return bot_reach

        current_depth=current_depth+1
        print("Increasing depth to " + str(current_depth))
        

    return None