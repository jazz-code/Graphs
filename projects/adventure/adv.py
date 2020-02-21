from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
# world.print_rooms()
print(f"RoomGraph: {room_graph[0][1]}")

player = Player(world.starting_room)
# print(player.current_room.get_exits())
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
new_graph = {}
# def bfs(starting_room, destination):
#   queue = Queue()
#   queue.enqueue([starting_room])
#   visited_rooms = set()
#   while queue.size() > 0:
#     path = queue.dequeue()
#     room_id = path[-1]
#     if room_id not in visited_rooms:
#       if room_id == destination:
#         return path
#       else:
#         for direction in room_graph[0]:
#           print(f"Room graph {graph[direction]}")
#           if graph[direction] != "?":
#             new_path = path.copy()
#             new_path.append(graph[direction])
#             queue.enqueue(new_path)
#       visited_rooms.add(room_id)
#     return []

# room_id = player.current_room.id 
# current_exits = player.current_room.get_exits()
# current = {}
# current['room_id'] = room_id
# print(f"Current: {current}")
# graph = {}
# if room_id not in graph:
#   new_room = {}
#   for direction in current_exits:
#       new_room[direction] = "?"
#   graph[room_id] = [new_room, current]
  
#   if room_id not in graph:
#     graph[current['room_id']][0][next_move] = room_id
#     graph[room_id] = {}
#     for direction in result['exits']:
#       graph[room_id][direction] = "?"
#     new_room = {}
#     for direction in result['exits']:
#       new_room[direction] = "?"
#     new_room[inverse_directions[next_move]] = current['room_id']
#     graph[room_id] = [new_room, result]

# inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}
# prev_move = None
# while len(visited_rooms) < len(room_graph):
#     # print(player.current_room)
#     current_exits = player.current_room.get_exits()
#     room_id = player.current_room.id
#     for direction in current_exits:
#       if room_id == target:
#         next_move = direction
#         break
#     else:
#         directions = []
#         for direction in current_exits:
#             # If adjacent room_id not visited yet, add that direction
#             if room_id == "?":
#                 directions.append(direction)
#         if len(directions) == 0:
#             print('All adjacent rooms visited..')
#             target = bfs(room_id, "?")
#             for direction in current_exits:
#                 if room_id == target:
#                     next_move = direction
#                     break
#             directions = [direction for direction in current_exits]
#             if len(directions) == 1:
#                 next_move = directions[0]
#             else:
#                 if prev_move is not None:
#                     directions.remove(inverse_directions[prev_move])
#                 next_move = random.choice(directions)
#         else:
#             next_move = random.choice(directions)
#             # print(f"Next move: {next_move}")
#     if player.travel([next_move]) == "?":
#         print(f"Traveling to the unknown.. ({len(new_graph)})")
#         end_room = player.travel(next_move)
#     else:
#         end_room = player.travel([next_move])
#         prev_move = next_move
#         current = end_room


# room_id = player.current_room.id 
# current_exits = player.current_room.get_exits()
# current = {}
# current['room_id'] = room_id
# print(f"Current: {current}")
# graph = {}
# if room_id not in graph:
#   new_room = {}
#   for direction in current_exits:
#       new_room[direction] = "?"
#   graph[room_id] = [new_room, current]
  
#   if room_id not in graph:
#     graph[current['room_id']][0][next_move] = room_id
#     graph[room_id] = {}
#     for direction in result['exits']:
#       graph[room_id][direction] = "?"
#     new_room = {}
#     for direction in result['exits']:
#       new_room[direction] = "?"
#     new_room[inverse_directions[next_move]] = current['room_id']
#     graph[room_id] = [new_room, result]

# bfs(current['room_id'], "?")

#     print(f"Graph: {graph[0]}")
#     current_exits = graph[0]
#     directions = []
#     for direction in current_exits:
#         # If adjacent room_id not visited yet, add that direction
#         if room_id == "?":
#             directions.append(direction)
#     if len(directions) == 0:
#         print('All adjacent rooms visited..')
#         target = bfs(graph, "?")
#         print(f"Current exits: {current_exits}")
#         for direction in current_exits:
#             if room_id == target:
#                 next_move = direction
#                 break
#         directions = [direction for direction in current_exits]
#         if len(directions) == 1:
#             next_move = directions[0]
#         else:
#             if prev_move is not None:
#                 directions.remove(inverse_directions[prev_move])
#             next_move = random.choice(directions)
#     else:
#         next_move = player.travel(random.choice(directions))
#     print(f'Next room: {current_exits}')
#     if next_move == "?":
#         print(f"Traveling to the unknown.. ({len(graph)}/500)")
#         end_room = player.travel(next_move)
#     else:
#         end_room = player.travel(next_move)
#     print("end_room: ",end_room)
#     prev_move = next_move
#     current = end_room


def newtraversal(player, world, graph):
    # Path list holds directions
    path_list = []
    s = []
    # Stack, holds player's current room
    s.append(player.current_room.id)
    visited_rooms = set()
    while len(visited_rooms) != len(world.rooms):
        # Get the current room
        current_room = s[-1]
        # Add the current room to visited
        visited_rooms.add(current_room)
        # Connecting room neighbors held in Queue
        q = []
        # Connecting room neighbors from graph
        neighbors = graph[current_room][1]
        # print(graph[current_room][1])
        # For unvisited rooms:
        for direction, room_id in neighbors.items():
            if room_id not in visited_rooms:
                q.append(room_id)
        # Get the next room from the Q while there are rooms
        if len(q) > 0:
            # Dequeue the next room
            # print(q)
            next_room = q[0]
            # Add it to the stack
            s.append(next_room)
        else:
            # The queue is empty, pop the current room from the stack
            s.pop()
            # Next room from the stack
            next_room = s[-1]
        # For any connected rooms
        for direction, room_id in neighbors.items():
            if room_id == next_room:
                path_list.append(direction)
    return path_list


traversal_path = newtraversal(player, world, room_graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# OLD TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# # print(player.)
# visited_rooms.add(player.current_room)
# while len(visited_rooms) < len(room_graph):
#     direction = random.choice(player.current_room.get_exits())
#     # Move in that direction
#     player.travel(direction)
#     # Log our room in our visited_rooms
#     visited_rooms.add(player.current_room)
#     # Log the direction in our traversal_path
#     traversal_path.append(direction)
# for move in traversal_path:
#     # print(traversal_path)
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