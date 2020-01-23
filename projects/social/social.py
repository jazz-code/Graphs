import random

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
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

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

        # Add users
        if num_users > avg_friendships:
            for user in range(0, num_users):
                # self.users[count] = self.friendships
                # print(self.users)
                # count += 1
                self.add_user(f"user {user + 1}")
                # print("user",self.users)
        else:
            raise IndexError("Users mist be greater than avg number of friendships")

        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            # Create a random friendship
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1

        print(f"Collisions: {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Note: Every means traversal
        visited = {}  # Note that this is a dictionary, not a set
        # Create queue
        queue = Queue()
        # Enqueue starting point in a list to start path
        queue.enqueue([user_id])
        # While queue not empty
        while queue.size() > 0:
            # Dequeue the path
            path = queue.dequeue()
            # Find the last vertex in path
            curr_user = path[-1]
            # If we havent visited this vertex
            if curr_user not in visited:
                # Do the thing!
                # Add to visited
                visited[curr_user] = path
                # Make new paths(copy) and enqueue for each vertex
                for friend_id in self.friendships[curr_user]:
                    new_path = list(path)
                    new_path.append(friend_id)
                    queue.enqueue(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("----------Printing Friendships----------")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("----------Printing Connections----------")
    print(connections)
