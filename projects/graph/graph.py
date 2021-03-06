# g = Graph()
# g.add_vertex('0')
# g.add_vertex('1')
# g.add_vertex('2')
# g.add_vertex('3')
# g.add_edge('0', '1')

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, and a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        # Add the starting vertex_id to the queue
        # Create an empty set to store visited nodes
        # While the queue is not empty...
            # Dequeue, the first vertex
            # Check if it's been visited
            # If it has not been visited...
                # Mark it as visited
                # Then add all neighbors to the back of the queue

        # Create an empty queue, and enqueue the starting vertex ID
        q = Queue()
        # Put the starting point in that
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited verticies
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            # print("here")
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop, the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # # Check if the node is visited
        # if visited is None:
        #     visited = set()
        # visited.add(starting_vertex)
        # print(starting_vertex)
        # for child_vert in self.vertices[starting_vertex]:
        #     if child_vert not in visited:
        #         self.dft_recursive(child_vert, visited)

        # Initislize visited if its not yet intialized
        if visited is None:
            visited = set()
        # Initislize path if its not yet intialized
        if path is None:
            path = []
        # Check if starting vertex has been visited
        # If not...
        if starting_vertex not in visited:
            # Mark it as visited, add to path
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            # If starting_vertex is destination:
            if starting_vertex == destination_vertex:
                # return path
                return path_copy
            #  Call DEFS recursive one each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                # path_copy = path.copy()
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add a PATH starting vertex_id to the queue
        path = q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            #  Grab the last vertx from the PATH
            v = path[-1]
            # Check if it's been visited
            if v not in visited:
                # Check if its the target
                if v == destination_vertex:
                    # if yes, return the path
                    return path
                # If it has not been visited...
                for next_vert in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack, and push the starting vertex ID
        s = Stack()
        # Add a PATH starting vertex_id to the stack
        path = s.push([starting_vertex])
        # Create an empty Set to store visited verticies
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            #  Grab the last vertx from the PATH
            v = path[-1]
            # Check if it's been visited
            if v not in visited:
                # Check if its the target
                if v == destination_vertex:
                    # if yes, return the path
                    return path
                # If it has not been visited...
                for neighbor in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)
    def dfs_recursive(self, starting_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        # Needs default args -- target_value, visited=None, path=None 
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # visited.add(starting_vertex)
        # path = path + [starting_vertex]
        # if starting_vertex == target_value:
        #     return path
        # for child_vert in self.vertices[starting_vertex]:
        #     if child_vert not in visited:
        #         new_path = self.dfs_recursive(child_vert, target_value, visited, path)
        #         if new_path:
        #             return new_path
        # return None
        pass
        # Check if the node is visited
        # if visited is None:
        #     visited = set()
        # # If not...
        # if starting_vertex not in visited:
        #     # Mark it as visited
        #     visited.add(starting_vertex)
        #     print(starting_vertex)
        #     # Call DFT recursive on each neighbor
        #     for neighbor in self.get_neighbors(starting_vertex):
        #         self.dft_recursive(neighbor, visited)
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print("Printing graph.vertices")
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("Running BFT")
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("Running DFT")
    graph.dft(1)
    # print("Running DFT recursive")
    # graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("Running BFS")
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("Running DFS")
    print(graph.dfs(1, 6))
    # print("Running DFS recursive")
    # print(graph.dfs_recursive(1, 6))
