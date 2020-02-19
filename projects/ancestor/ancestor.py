from graph import Graph
from util import Queue
from util import Stack

# 1. Translate the problem into graph terminology
    # We want to BFS the fartest distance to the end, returning the lowerest numeric ID
# 2. Build your graph
# 3. Traverse your graph

# def earliest_ancestor(ancestors, starting_node, visited=set(), path=[]):
#     '''
#     Given the dataset and the ID of an individual in the dataset,
#     returns their earliest known ancestor – the one at the farthest distance from the input individual.
#      If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
#      If the input individual has no parents, the function should return -1.
#     '''
#     graph = Graph()
#     # For each pair in ancestors
#     for pair in ancestors:
#         # add pair nodes to graph
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # add its edges in reverse, cuz we want to target node parents, upwards!
#         graph.add_edge(pair[0], pair[1])
#     print(f'verticies: {graph.vertices}') 
            
#     # Create an empty queue
#     queue = Queue()
#     # Add the initial vertex to the path
#     path.append(starting_node)
#     # Then add the path to the queue, should be initialized as a empty list
#     queue.enqueue(path)
#     # While the queue is not empty...
#     while queue.size() > 0:
#         # Dequeue, the first PATH
#         path = queue.dequeue() 
#         # GRAB THE LAST VERTEX FROM THE PATH
#         last_vertex = path[-1] 
#         # else check if it's been visited
#         if last_vertex not in visited:
#         # If it has not been visited...
#             # Add it to the visited dic
#             visited.add(last_vertex)
#             print("here")
#             # iterate over the last vertex's neighbors..
#             for neighbor in graph.get_neighbors(last_vertex):
#                 # we check if the neighbor is NOT marked as visited...
#                 if neighbor not in visited:
#                     # if it is not, we make a copy of the path
#                     path_copy = path.copy()
#                     # we append the neighbor to the copy of the path
#                     path_copy.append(neighbor)
#                     # then we add the copy of the path to the queue
#                     queue.enqueue(path_copy)
#     return print(last_vertex)
#     # if the vertex set is empty..
#     if bool(graph[last_vertex]) is False:
#         # we return -1
#         return -1
#     else:
#         # else we return the last vertex
#         return last_vertex


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
        # If the path is longer or equal and the value is smaller, 
        # or if the path is longer, update the ancestor and longer path
        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
                # set the earliest ancestor to the node
                # print("here")
                earliest_ancestor = v
                print(earliest_ancestor)
                # set the max path length to the len of the path
                max_path_length = len(path)
        # Then add all neighbors to the back of the queue
        for neighbor in g.get_neighbors(v):
            path_copy = path.copy()
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor



ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(ancestors, 1)










