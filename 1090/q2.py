# https://codeforces.com/problemset/problem/1899/A

import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    _ = input()
    nums = [int(elem) for elem in input().split()]
    """
    prefix = -3
    lowest = -3
    result = -inf
    parity = 0
    -2 -1
       ^
    """
    prefix = 0
    lowest = float("inf")
    result = float("-inf")
    # 0 = even
    # 1 = odd
    parity = nums[0] % 2
    for i in range(len(nums)):
        curr_num = nums[i]
        if curr_num % 2 == parity:
            prefix = curr_num
            lowest = curr_num
            result = max(prefix, result)
        else:
            prefix += curr_num
            result = max(prefix, prefix - lowest, result)
            lowest = min(lowest, prefix)
        parity = curr_num % 2
    print(result)


"""
1
5
1 2 3 4 5

prefix = -1
lowest = -1
result = -1
-1 -1
^

expected = -1


Find the max sum of a non empty subarray.

find subarrays that alternate.. Count the sum..

-1 4 -1 0 5 -4
3
8

Brute force is just O(n^2). idk if we can do that for 10^5



"""
# STUDY THIS CODE AFTER!!! LEARN KADANES!!!!!
import sys
input = sys.stdin.readline
tests = int(input())
for  in range(tests):
     = input()
    nums = [int(elem) for elem in input().split()]
    res = nums[0]
    parity = nums[0] % 2
    cur = nums[0]
    for i in range(1, len(nums)):
        if nums[i] % 2 == parity or cur < 0:
            cur = 0
        parity = nums[i] % 2
        cur += nums[i]
        if cur > res:
            res = cur
    print(res)