import sys
input = sys.stdin.readline
tests = int(input())

# first = input().split()
for _ in range(tests):
    first = input().split()
    s = int(first[1])
    x = int(first[2])
    second = sum([int(elem) for elem in input().split()])
    # print(second, s)
    diff = s - second
    if diff == 0:
        print("YES")
    elif diff < 0:
        print("NO")
    elif diff % x == 0:
        print("YES")
    else:
        print("NO")

"""
1
3 3 5
1 1 1
"""