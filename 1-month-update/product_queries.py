import sys
import math
input = sys.stdin.readline
tests = int(input())


# first = input()
for _ in range(tests):
    n = int(input())

    memo = [float("inf") for i in range(n)]
    for elem in input().split():
        memo[int(elem) - 1] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            memo[j - 1] = min(memo[j - 1], memo[i - 1] + memo[j // i - 1])
    
    print(" ".join([str(elem) if elem != float("inf") else "-1" for elem in memo]))

"""
1
8
3 2 2 3 7 3 6 7

Array a
given n question

min number of elements to equal i.. Or report that it's impossible to achieve


"""