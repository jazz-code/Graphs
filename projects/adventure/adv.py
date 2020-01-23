from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

def dfs(self, starting_room, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    traversal_path = []
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)
    # Create a queue/stack as appropriate
    stack = Stack()
    starting_room = player.current_room.id
    print("starting room: ",starting_room)
    # Put the starting point in that
    # Enstack a list to use as our path
    stack.push([starting_room])
    # Make a set to keep track of where we've been
    visited = set()
    # While there is stuff in the queue/stack
    while stack.size() > 0:
    #    Pop the first item
        traversal_path = stack.pop()
        vertex = path[-1]
    #    If not visited
        if vertex not in visited:
            if vertex == destination_vertex:
                # Do the thing!
                return traversal_path
            visited.add(vertex)
    #       For each edge in the item
            # for next_vert in self.get_neighbors(vertex):
            # # Copy path to avoid pass by reference bug
            #     new_path = list(traversal_path) # Make a copy of path rather than reference
            #     new_path.append(next_vert)
            #     stack.push(new_path)
          
            # for move in traversal_path:
            #     player.travel(move)
            #     visited_rooms.add(player.current_room)
            # if len(visited_rooms) == len(room_graph):
            #     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
            # else:
            #     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
            #     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
