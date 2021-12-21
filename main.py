from originalGraph import generate_graph_params
from testUCS import uniform_cost_search
from IDS import IDS


if __name__ == "__main__":
    
    #Uniform Cost Search
    cost = True
    standard_cost = 1
    door_cost = 2
    path_ucs, explored_ucs = uniform_cost_search(generate_graph_params(cost), '0', '92', standard_cost, door_cost)
    print("============ UCS Search ================")
    print("Path UCS:", path_ucs)

    #Iterative Deepening Search
    cost = False
    traversal_path = []
    traversal_path = IDS(generate_graph_params(cost), '0','92',traversal_path)
    print("============ IDS Search ================")
    print("Path IDS:", traversal_path)

    #A star Search

    


