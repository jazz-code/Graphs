from graph import Graph
from util import Queue


def earliest_ancestor(ancestors, starting_node):
    #Build Graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        #Build edges in reverse
        graph.add_edge(pair[0], pair[1])
    #Do a BFS (stores path)
    q =Queue()
    #Enqueue list for building paths
    q.enqueue([starting_node])
    #Longest path so far
    max_path_len = 1
    #Earliest ancestor so far
    earliest_ancestor = -1
    #BFS
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        #If the path is longer or equal and the value is smaller, or path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
        return earliest_ancestor
















