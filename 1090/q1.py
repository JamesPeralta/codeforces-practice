# https://codeforces.com/problemset/problem/1899/A

import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    first = int(input())
    if first % 3 == 0:
        print("Second")
    else:
        print("First")



"""
if integer is divisible by 3 then he VA wins

n = 1, Vanya wina

n = 3, Vova wins

0, 3, 6, 9


"""