# Pattern: Simulation with lazy reset — track resets and last_reset per index; on update only reset an index if it was reset in a previous global reset; when value > h, do global reset and set that index to init
import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    first = [elem for elem in input().split()]
    n, m, h = int(first[0]), int(first[1]), int(first[2])
    arr = []
    init_arr = []
    resets = 0
    last_reset = []

    for elem in input().split():
        elem = int(elem)
        arr.append(elem)
        init_arr.append(elem)
        last_reset.append(0)
        
    for _ in range(m):
        third = input().split()
        index, delta = int(third[0]), int(third[1])
        index = index - 1
        if last_reset[index] < resets:
            arr[index] = init_arr[index]
            last_reset[index] = resets
        
        arr[index] += delta
        if arr[index] > h:
            resets += 1
            last_reset[index] = resets
            arr[index] = init_arr[index]

    for i in range(len(arr)):
        if last_reset[i] < resets:
            arr[i] = init_arr[i]

    print(" ".join([str(elem) for elem in arr]))