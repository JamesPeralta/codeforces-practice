import sys
input = sys.stdin.readline
tests = int(input())

for _ in range(tests):
    _ = int(input())
    nums = [int(elem) for elem in input().split()]

    is_inc = True
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            is_inc = False
            break

    if is_inc:
        print(len(nums))
    else:
        print(1)