from collections import deque
tests = int(input())
for _ in range(tests):
    _, start = input().split()
    arr = input()

    # greens = deque([])
    # seen = set()
    # for i, elem in enumerate(arr):
    #     if elem == "g":
    #         greens.append((i, 0))
    #         seen.add(i)

    # furthest = {"g": float("-inf"), "r": float("-inf"), "y": float("-inf")}
    # while greens:
    #     index, dist = greens.popleft()
    #     # print(index)
    #     furthest[arr[index]] = max(furthest[arr[index]], dist)

    #     left, right = (index - 1) % len(arr), (index + 1) % len(arr)
    #     if left not in seen:
    #         greens.append((left, dist + 1))
    #         seen.add(left)

    #     if right not in seen:
    #         greens.append((right, dist + 1))
    #         seen.add(right)

    index = arr.index("g")
    furthest = {"g": float("-inf"), "r": float("-inf"), "y": float("-inf")}
    last_green = 0
    for i in range(len(arr)):
        curr_i = (index - i) % len(arr)
        if arr[curr_i] == "g":
            last_green = 0
        else:
            last_green += 1
        
        furthest[arr[curr_i]] = max(furthest[arr[curr_i]], last_green)
    
    # print(furthest)
    print(furthest[start])



"""
rrg
120   

rgr
201

   0   0
rrrgyyygy

"""