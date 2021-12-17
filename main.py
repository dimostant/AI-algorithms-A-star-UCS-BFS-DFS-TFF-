#from testGraph import graph_neighbours
#from UCS import ucs
from originalGraph import graph_neighbours
from testUCS import uniform_cost_search


if __name__ == "__main__":
    standard_cost = 1
    door_cost = 2
    print("============ UCS Search ================")
    path_ucs, explored_ucs = uniform_cost_search(graph_neighbours, '55', '92', standard_cost, door_cost)
    #path_ucs = ucs(graph_neighbours, '0', '92')
    print("Path UCS:", path_ucs)
    #print("Explored Nodes UCS: ", explored_ucs)
    #print(len(explored_ucs))
    #print()
    
    


