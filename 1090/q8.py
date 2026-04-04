import sys
input = sys.stdin.readline
tests = int(input())
# https://codeforces.com/problemset/problem/1827/A
for _ in range(tests):
    first = ["2"] * int(input())
    _ = input()
    
    if len(first) == 1:
        print("1")
    else:
        print(" ".join(first))



"""

"""