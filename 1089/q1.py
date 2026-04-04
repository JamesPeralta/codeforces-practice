import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    n = int(input())
    result = []
    for i in range(n, 0, -1):
        result.append(str(i))

    print(" ".join(result))


"""

"""