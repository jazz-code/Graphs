import random

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
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i + 1}")
        # Create friendships
        # Create a list w/ all possible friendships
        possible_friendships = []
        for user_id in self.users:
            #Larger than friend_id
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        print(f"possible friendships {possible_friendships}")
        
        # Shuffle the list
        random.shuffle(possible_friendships)
        # Grab the first N total_friendships pairs form the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            frienship = possible_friendships[i]
            self.add_friendship(frienship[0], frienship[1])
        # Avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        #  N = total_friendships // 2
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        s = Stack()
         # Add the starting vertex_id to the stack
        s.push([user_id])
        # Create an empty set to store visited nodes
        visited = {}  # Note that this is a dictionary, not a set
        # While the stack is not empty...
        while s.size() > 0:
            # Pop, the first vertex
            path = s.pop()
            user = path[-1]
            # Check if it's been visited
            # If it has not been visited...
            if user not in visited:
                # Mark it as visited
                visited[user] = path
                # Then add all neighbors to the top of the stack
                for friend in self.friendships[user]:
                    copy_path = path.copy()
                    copy_path.append(friend)
                    s.push(copy_path)
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    # print(f"Users: {sg.users}")
    print(f"friendships: {sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"Connections: {connections}")
