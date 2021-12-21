from graph import generate_graph_params
from UCS import uniform_cost_search
from IDS import IDS
from A_Pathfinding import Apathfinding


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
    graph_neighbours = [
        ['1', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '1', '0'],  # row(0,12)
        ['1', '1', '1', '2', '0', '1', '1', '1', '1', '1', '2', '1', '0'],  # row(1,12)
        ['0', '1', '0', '1', '1', '1', '1', '0', '0', '1', '0', '1', '0'],  # row(2,12)
        ['1', '1', '2', '0', '1', '2', '0', '1', '1', '2', '1', '1', '1'],  # row(3,12)
        ['0', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '0', '1'],  # row(4,12)
        ['1', '2', '1', '0', '1', '0', '1', '1', '0', '0', '1', '1', '1'],  # row(5,12)
        ['0', '1', '2', '0', '1', '0', '0', '2', '1', '1', '2', '0', '2'],  # row(6,12)
        ['1', '0', '1', '1', '2', '1', '1', '1', '0', '1', '1', '1', '1'],  # row(7,12)
        ['1', '1', '2', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1'],  # row(8,12)
        ['0', '0', '1', '1', '1', '1', '0', '1', '1', '1', '1', '1', '2'],  # row(9,12)
        ['0', '0', '1', '0', '0', '1', '1', '2', '0', '0', '0', '1', '1'],  # row(10,12)
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']   # row(11,12)
    ]

    print("============= A* Search ================")
    path = Apathfinding(graph_neighbours, (0,0), (10, 12))
    print('Path A* :', path)

    


