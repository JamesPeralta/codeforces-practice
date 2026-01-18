from collections import defaultdict
from bisect import bisect_left

tests = int(input())

def closest_left(mines, target):
    left, right = 0, len(mines)
    while left < right:
        mid = left + ((right - left) // 2)
        if mines[mid] >= target:
            right = mid - 1
        else:
            left = mid
    return float("-inf") if mines[left] > target else mines[left]

def closest_right(mines, target):
    left, right = 0, len(mines)
    while left < right:
        mid = left + ((right - left) // 2)
        if mines[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return float("inf") if mines[left] < target else mines[left]

for _ in range(tests):
    first = input().split()
    robots, spikes , instructions = int(first[0]), int(first[1]), int(first[2])
    robots = []
    for i, elem in enumerate(input().split()):
        robots.append(int(elem))
    spikes = [int(elem) for elem in input().split()]
    spikes.sort()

    moves = input()
    # Compress movements
    seen = {0: 0}
    pos = 0
    for index, elem in enumerate(moves):
        pos += -1 if elem == "L" else 1
        if pos not in seen:
            seen[pos] = index + 1

    closest = [[]]
    deads = [0 for i in range(instructions)]
    for robot in robots:
        left = closest_left(spikes, robot)
        right = closest_right(spikes, robot)
        delta_left = (robot - left) * -1
        delta_right = right - robot


        seen_left = float("inf") if delta_left not in seen else seen[delta_left]
        seen_right = float("inf") if delta_right not in seen else seen[delta_right]
        dead = min(seen_left, seen_right)
        if dead != float("inf"):
            deads[dead - 1] += 1
            
    for i in range(1, len(deads)):
        deads[i] += deads[i- 1]
    
    for i in range(len(deads)):
        deads[i] = str(len(robots) - deads[i])
    print(" ".join(deads))


"""
what's the fastest way to see the closest robot
to my left.. probably binary search

1
2 1 3
0 1
2
LRR

LLR ends at 1.. but seen 2

LRL ends at 1.. but only seen 1


Can just simulate this
"""