

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]:[] for user in users}

for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def totalNoOfConnections(friendships):
    totalConnections = sum(len(friends) 
    for friends in friendships.values())
    avgConnections = totalConnections / (len(friendships.keys()))
    print(totalConnections)
    print(avgConnections)
    
totalNoOfConnections(friendships)

def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users


def sortFriends(friendships):
    tup = {(key,len(value)) 
    for key, value in friendships.items()}

    sortedtup = sorted(tup, key=lambda x: x[1], reverse = True)
    print(tup)
    print(sortedtup)
sortFriends(friendships)
