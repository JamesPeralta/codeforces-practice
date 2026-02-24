"""
b is some array

b = [1, 2, 4, 8]
a = [2, 4, 16, 256]

two subarrays that equal the same?
"""

tests = int(input())

for _ in range(tests):
    _ = input()
    nums = input().split()
    dupes = set()

    for num in nums:
        dupes.add(num)

    if len(dupes) == len(nums):
        print("NO")
    else:
        print("YES")