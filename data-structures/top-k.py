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

Solution without custom class: use key (-rating, -lastActive, user_id).
"""
import heapq

users = [
    (1, 10, 1),
    (2, 10, 1),
    (3, 23, 1),
    (4, 23, 5),
    (5, 100, 5),
]

def k_best_fn(k):
    # Key so *worse* user = smaller = evicted when len > k: (rating, ts, -user_id)
    # (lower rating, older ts, larger id → smaller key)
    k_best = []
    for user_id, rating, ts in users:
        key = (rating, ts, -user_id)
        heapq.heappush(k_best, (key, user_id))
        if len(k_best) > k:
            heapq.heappop(k_best)

    # Drain: we get worst-first, reverse for best-first.
    result = []
    while k_best:
        _, user_id = heapq.heappop(k_best)
        result.append(user_id)
    result.reverse()
    return result

if __name__ == "__main__":
    print(k_best_fn(4))  # [5, 4, 3, 1] — top 4 by rank
