from graph import Graph
from util import Queue
from util import Stack

# 1. Translate the problem into graph terminology
    # We want to BFS the fartest distance to the end, returning the lowerest numeric ID
# 2. Build your graph
# 3. Traverse your graph

def earliest_ancestor(ancestors, starting_node):
    '''
    Given the dataset and the ID of an individual in the dataset,
    returns their earliest known ancestor – the one at the farthest distance from the input individual.
     If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
     If the input individual has no parents, the function should return -1.
    '''
    #Build Graph
    g = Graph()
    # For each pair in ancestors
    for pair in ancestors:
        # add pair nodes to graph
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        # add its edges in reverse, cuz we want to target node parents, upwards!
        g.add_edge(pair[0], pair[1])
    print(f'verticies: {g.vertices}') 
    # Create an empty queue
    q = Queue()
    # Add the starting vertex_id to the sueue
    q.enqueue([starting_node])
    # intialize max_path_length to 1
    max_path_length = 1
    # intialize first ancestor to -1
    earliest_ancestor = -1
    # While the sueue is not empty...
    while q.size() > 0:
        # Dequeue, the first vertex
        path = q.dequeue()
        # v is last in path
        v = path[-1]
        print("here")
        # Check if it's been visited
        # If it has not been visited...
        # if v not in visited:
            # if v == ancestors:
            # # Mark it as visited
            #     print(path)
            #     return path[-1]
        # If the path is longer or equal and the value is smaller, 
        # or if the path is longer, update the ancestor and longer path
        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
                # set the earliest ancestor to the node
                # print("here")
                earliest_ancestor = v
                # set the max path length to the len of the path
                max_path_length = len(path)
        # Then add all neighbors to the back of the queue
        for neighbor in g.get_neighbors(v):
            path_copy = path.copy()
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor



ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(ancestors, 1), 10

# g = Graph()
# for pair in ancestors:
#     g.add_vertex(pair[0])
#     # print(g.vertices)
#     g.add_vertex(pair[1])
#     # print(g.vertices)
#     g.add_edge(pair[0], pair[1])
# print("Printing graph.vertices")
# print(g.vertices)










