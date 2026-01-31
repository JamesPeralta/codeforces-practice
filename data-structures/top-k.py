"""
Problem: Top K Users on LeetCode

You’re given a list of users.

Each user has:
- id (string)
- rating (integer)
- lastActive (integer timestamp; larger = more recent)

Define a user’s rank as:
 1. Higher rating ranks higher.
 2. If two users have the same rating, the one with more recent lastActive ranks higher.
 3. If both rating and lastActive are the same, break ties by lexicographically smaller id ranking higher (to make the ordering total and deterministic.

Task: Return the k largest users by this ranking.

Example

(user_id, rating, lastActive)
users = [
    (1, 10, 1),
    (2, 10, 1),
    (3, 23, 1),
    (4, 23, 5),
    (5, 100, 5),
]

h           l
5, 4, 3, 1, 2

Probably define a User class with those properties

__lt__

 if rating is diff

 elif lastActive diff

 else:
    return self.user_id > a.user_id   # larger id = lower rank = "smaller" for min-heap
"""
import heapq

class User:
    def __init__(self, user_id, rating, last_active):
        self.user_id = user_id
        self.rating = rating
        self.last_active = last_active
    
    def __lt__(self, elem):
        if self.rating != elem.rating:
            return self.rating < elem.rating
        elif self.last_active != elem.last_active:
            return self.last_active < elem.last_active
        else:
            return self.user_id > elem.user_id

    def __repr__(self):
        return f"{self.user_id}"

users = [
    (1, 10, 1),
    (2, 10, 1),
    (3, 23, 1),
    (4, 23, 5),
    (5, 100, 5),
]

def k_best_fn(k):
    print("Hello World")
    k_best = []
    for user_id, rating, ts in users:
        heapq.heappush(k_best, User(user_id, rating, ts))
        if len(k_best) > k:
            heapq.heappop(k_best)
    
    result = []
    while len(k_best):
        result.append(heapq.heappop(k_best))
    
    result.reverse()
    print(result)

k_best_fn(4)
