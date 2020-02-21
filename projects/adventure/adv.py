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
print(f"RoomGraph: {room_graph[0]}")
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print(player.current_room.get_exits())
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def bfs(starting_room, destination):
  queue = Queue()
  player.current_room.id = starting_room
  queue.enqueue([starting_room])
  visited_rooms = set()
  while queue.size() > 0:
    path = queue.dequeue()
    room_id = path[-1]
    if room_id not in visited_rooms:
      if room_id == destination:
        return path
      else:
        for direction in room_graph:
        #   print(f"Room graph {room_graph[direction]}")  
          if room_graph[direction] != "?":
            new_path = path.copy()
            new_path.append(room_graph[direction])
            queue.enqueue(new_path)
      visited_rooms.add(room_id)
    return []
bfs(0,2)
inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}
prev_move = None
while True:
    # print(player.current_room)
    current_exits = player.current_room.get_exits()
    room_id = player.current_room.id
    target = bfs(player.current_room.id, 3)
    print(f'Traversing to target...')
    for direction in current_exits:
      if room_id == target:
        next_move = direction
        break
    else:
        directions = []
        for direction in current_exits:
            # If adjacent room_id not visited yet, add that direction
            if room_id == "?":
                directions.append(direction)
        if len(directions) == 0:
            print('All adjacent rooms visited..')
            target = bfs(room_id, "?")
            for direction in current_exits:
                if room_id == target:
                    next_move = direction
                    break
            directions = [direction for direction in current_exits]
            if len(directions) == 1:
                next_move = directions[0]
            else:
                if prev_move is not None:
                    directions.remove(inverse_directions[prev_move])
                next_move = random.choice(directions)
        else:
            next_move = random.choice(directions)
        print(f'Next room: {player.travel([next_move])}')
        print(f'Room [{room_id}] to Room [{player.travel([next_move])}]')
        if player.travel([next_move]) == "?":
            print(f"Traveling to the unknown.. ({len(room_graph)}/500)")
            end_room = player.travel(next_move)
        else:
            end_room = player.travel([next_move])
            prev_move = next_move
            current = end_room


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
# print(player.)
visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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