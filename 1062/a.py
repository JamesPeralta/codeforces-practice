part1, part2 = input(), input()
# print(part1)
# print(part2)

"""
6
1 3 4 5 6 9

9
1 4 5 6 7 100 101 102 103
Output
4
Answer
2
Checker Log
wrong answer 1st numbers differ - expected: '2', found: '4'
"""

nums = list(map(int, part2.split()))
# print(nums)
nums.append(1001)

result = 0
increasing_length = 1
for index, num in enumerate(nums):
    # print(increasing_length)
    if index == 0:
        if num == 1:
            increasing_length += 1
    else:
        if num == nums[index - 1] + 1:
            increasing_length += 1
        else:
            if increasing_length >= 3:
                result = max(result, increasing_length - 2)
            increasing_length = 1

if increasing_length >= 3:
    result = max(result, increasing_length - 2)
print(result)