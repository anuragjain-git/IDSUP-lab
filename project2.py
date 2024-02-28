users= [
    { "id": 0, "name": "Ashok" },
    { "id": 1, "name": "Rahul" },
    { "id": 2, "name": "Sarita" },
    { "id": 3, "name": "Rohan" },
    { "id": 4, "name": "Akhaya" },
    { "id": 5, "name": "Prakash" },
    { "id": 6, "name": "Madhabi" },
    { "id": 7, "name": "Spandan" },
   
]

Interests = [
    (0, "python"), (0, "java"), (1, "java"), (2, "python"),
    (2, "java"), (3, "python"), (4, "c"),
    (5, "c"), (6, "python"), (7, "java")
]

'''Find the list of user ids by interest'''
def users_by_interests(interest):
    return [user_id for user_id, interest_name in Interests if interest_name == interest ]


InterestName  = "Java"
print(f"List of user ids by interest Interest = {InterestName}")
print(users_by_interests(InterestName))


'''Find the list of interests by user id'''
def interest_byUserId(userId):
    return [interest_name for user_id, interest_name in Interests if user_id == userId ]

userId = 0
print(f"List of uof interests by user id for user id = {userId }")
print(interest_byUserId(userId ))



'''Find who has the most interest in common with a given user.'''
def most_interests_in_common(user_id):
    max_common_interests = 0
    user_interests = set(interest_byUserId(user_id))

    for user in users:
        if user['id'] != user_id:
            common_interests = len(set(interest_byUserId(user['id'])) & user_interests)
            if common_interests > max_common_interests:
                max_common_interests = common_interests
                most_common_user = user['name']

    return most_common_user

userCid = 1
print(f"user who has the most interest in common with a given user with id = {userCid}")
print(most_interests_in_common(userCid))





