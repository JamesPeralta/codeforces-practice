import sys
input = sys.stdin.readline
tests = int(input())

# first = input()
for _ in range(tests):
    first = input().split()
    queries = int(first[1])
    a = [int(elem) for elem in input().split()]

    for index, elem in enumerate(input().split()):
        a[index] = max(a[index], int(elem))
    
    largest = a[-1]
    for i in range(len(a) - 1, -1, -1):
        largest = max(largest, a[i])
        a[i] = largest
    
    prefix_sum = []
    for i in range(len(a)):
        if i == 0:
            prefix_sum.append(a[i])
            continue
        # print()
        prefix_sum.append(a[i] + prefix_sum[-1])

    # print(a, prefix_sum)
    result = []
    for _ in range(queries):
        second = input().split()
        l, r = int(second[0]), int(second[1])
        # print(r, l)
        r = prefix_sum[r - 1]
        l = 0 if l - 2 < 0 else prefix_sum[l - 2]
        # print(r, l)
        result.append(str(r - l))
    
    print(" ".join(result))

"""
3 1 ->n and q
3 2 1 -> a
1 2 3 -> b
1 3 -> the query
"""