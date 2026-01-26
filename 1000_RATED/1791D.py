"""
     3 2 1
abcabcd


"""
tests = int(input())

for b in range(tests):
    _ = input()
    arr = input()
    distinct = set()
    suffix = [0 for i in range(len(arr))]
    for i in range(len(arr) - 1, -1, -1):
        distinct.add(arr[i])
        suffix[i] = len(distinct)

    distinct = set()
    result = 0
    for i in range(len(arr) - 1):
        distinct.add(arr[i])
        # print(len(distinct), suffix)
        result = max(result, len(distinct) + suffix[i + 1])

    print(result)

"""
1
7
abcabc
"""