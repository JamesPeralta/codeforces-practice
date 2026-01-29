import sys
import bisect
input = sys.stdin.readline
tests = int(input())

def bsearch(arr, l, r, target):
    l, r = 0, len(arr)
    while l < r:
        mid = l + ((r - l) // 2)
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    
    return l

# first = input()
for _ in range(tests):
    first = input()
    swords = [int(elem) for elem in input().split()]
    swords.sort()
    levels = [int(elem) for elem in input().split()]
    prefix_sum = []
    curr_sum = 0
    for elem in levels:
        curr_sum += elem
        prefix_sum.append(curr_sum)

    best_res = 0
    # print(swords, prefix_sum)
    for i, difficul in enumerate(swords):
        # strength of swords
        left = len(swords) - i
        passed = bisect.bisect_right(prefix_sum, left)
        # print(difficul, "bisect", passed)
        best_res = max(best_res, difficul * passed)
    print(best_res)
"""
1
3
1 3 4
2 1 1

n swords each with a certain strength

game has n levels

each level you need to deal it bi strikes

sword less than x will not affect monsters..

score is x multiplied by

Maximize the game score

swords = 1, 2, 3, 4

swords you pick affect number of levels you can do


1
3 <- levels
1 3 4 <- swords
  ^
2 1 1 <- strikes

2 3 4 <- swords to reach this level..
"""
 