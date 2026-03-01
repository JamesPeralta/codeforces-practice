import sys
from collections import Counter

input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    x = input()

    nums = [int(elem) for elem in input().split()]
    count = Counter(nums)
    maxi = max(nums)
    print(count[maxi])