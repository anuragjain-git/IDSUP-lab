#1.	Find the list of user ids by interest

#2.	Find the list of interests by user id

#3.	Find who has the most interest in common withÂ aÂ givenÂ user.
users=[
    {'id':0,'name':'Ashok'},
    {'id':1, 'name':'Rahul'},
    {'id':2, 'name':'Sarita'},
    {'id':3, 'name':'Rohan'},
    {'id':4, 'name':'Akhaya'},
    {'id':5, 'name':'Prakash'},
    {'id':6, 'name':'Madhabi'},
    {'id':7, 'name':'Spandan'}
   
    ]

interests=[(0,'python'),(0,'java'),(1,'java'),(2,'python'),(2,'java'),(3,'python'),(4,'c'),(5,'c'),(6,'python'),(7,'java')]

from collections import defaultdict
from collections import Counter
 
user_ids_by_interest= defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
interests_by_user_id=defaultdict(list)
for user_id, interest in interests:
   interests_by_user_id[user_id].append(interest)
   
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"])
for user in users:
    print(most_common_interests_with(user))
