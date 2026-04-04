import sys
input = sys.stdin.readline
tests = int(input())
# https://codeforces.com/problemset/problem/1875/A
for _ in range(tests):
    first = input().split()
    a, b, n = int(first[0]), int(first[1]), int(first[2])
    nums = [int(elem) for elem in input().split()]

    result = b - 1
    for num in nums:
        result += min(1 + num, a) - 1

    print(result + 1)

"""
a = cap
b = initial value
n = tools


intuition = use the larger values later

the maximum time in seconds until the bomb explodes.

b

let it drop to 1

start = b - 1 

start += min(1+tool[i], a) - 1


"""