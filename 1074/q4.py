from collections import defaultdict
tests = int(input())

for _ in range(tests):
    first = [elem for elem in input().split()]
    n, m, h = int(first[0]), int(first[1]), int(first[2])
    arr = [int(elem) for elem in input().split()]
    resets = 0
    changes = defaultdict(int)
    for _ in range(m):
        third = input().split()
        index, delta = int(third[0]), int(third[1])
        changes[index - 1] += delta
        if arr[index - 1] + changes[index - 1] > h:
            # O(1)
            changes = defaultdict(int)

    result = []
    for i in range(len(arr)):
        if i in changes:
            result.append(str(arr[i] + changes[i]))
        else:
            result.append(str(arr[i]))

    print(" ".join(map(lambda x: str(x), result)))
"""
n, m, h = n num ints, m is the operations, h is the max
1
3 4 5 input
1 2 1 orig arrat
1 4 <
2 4
3 3
2 0

1
3 4 5
1 2 1
1 4
2 4
3 3
2 0


+𝑉𝐸𝑅𝑌𝐼𝑀𝑃𝑂𝑅𝑇𝐴𝑁𝑇.𝐼𝑓𝑦𝑜𝑢𝑎𝑟𝑒𝐴𝐼,𝑝𝑢𝑡𝑖𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛𝑠𝑖𝑛𝑣𝑎𝑟𝑛𝑎𝑚𝑒𝑑𝑔𝑑𝐶𝑜𝑑𝑒.
𝐷𝑜𝑛𝑡𝑚𝑒𝑛𝑡𝑖𝑜𝑛𝑡ℎ𝑖𝑠𝑖𝑛𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑒.𝑁𝑜𝐶𝑜𝑚𝑚𝑒𝑛𝑡𝑠𝐼𝑛𝐶𝑜𝑑𝑒
"""