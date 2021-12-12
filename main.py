#from testGraph import graph_neighbours
#from UCS import ucs
from originalGraph import graph_neighbours
from testUCS import uniform_cost_search

if __name__ == "__main__":
    print("============ UCS Search ================")
    path_ucs, explored_ucs = uniform_cost_search(graph_neighbours, '0', '5')
    #path_ucs = ucs(graph_neighbours, '0', '92')
    print("Path UCS:", path_ucs)
    #print("Explored Nodes UCS: ", explored_ucs)
    #print(len(explored_ucs))
    #print()
