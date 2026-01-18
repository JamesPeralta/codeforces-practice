"""
Get to pupil... what math should I learn?

Or 

Heap problem

push all elements onto the heap..
max heap.. 

pop out max with smallest index
"""
import heapq
tests = int(input())

for _ in range(tests):
    first = input().split()
    k = int(first[1])
    second = [int(elem) for elem in input().split()]

    heap = []
    for i in range(len(second)):
        heapq.heappush(heap, (second[i] * -1, i))
    
    result = []
    while heap:
        # print(heap)
        curr, index = heapq.heappop(heap)
        curr = curr * -1
        # print("Largest", curr, "at", index)
        curr -= k
        if curr > 0:
            heapq.heappush(heap, (curr * -1, index))
        else:
            result.append(str(index + 1))
    print(" ".join(result))

"""
1
3 2
1 2 3


k = 2
1 2 3
    ^
    
"""