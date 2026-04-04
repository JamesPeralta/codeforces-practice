import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
tests = int(input())
"""
1
5
20 5 1 4 2
"""
for _ in range(tests):
    _ = input()
    nums = [(int(elem), index) for index, elem in enumerate(input().split())]
    nums.sort()

    # print(nums)

    prefix = []
    for num, _ in nums:
        if len(prefix) == 0:
            prefix.append(num)
        else:
            prefix.append(num + prefix[-1])

    # print(prefix)
    
    """
    1
    5
    20 5 1 4 2
    """
    result = [None for _ in range(len(nums))]
    curr_index = 0
    for num, result_index in nums:
        # print("_______", num)
        score = prefix[curr_index]
        j = curr_index
        while j < len(nums):
            next_ind = bisect_right(nums, (score + 1, float("-inf"))) - 1
            if j == next_ind:
                break
            else:
                j = next_ind
                score = prefix[j]

        curr_index += 1
        result[result_index] = str(j)
    print(" ".join(result))
