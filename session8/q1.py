"""


"""
tests = int(input())


for _ in range(tests):
    first = input().split()
    arr = [int(elem) for elem in input().split()]
    x = int(first[1])
    arr.append(0)
    arr.sort()
    longest_dist = float("-inf")

    dist = x - arr[-1]
    arr.append(x + dist)
    # print(arr)
    for i in range(len(arr) - 1):
        longest_dist = max(longest_dist, arr[i + 1] - arr[i])

    print(longest_dist)
