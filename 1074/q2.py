tests = int(input())

for _ in range(tests):
    n = int(input())
    second = [int(elem) for elem in input().split()]

    print(n * max(second))
"""
2 1 4 5 3


"""