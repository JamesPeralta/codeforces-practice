"""
5
1 2 93 84 2


- for each element - figure out how many elements to the right are larger or smaller.
  choose max

Find a k where this element is 

choose a random k

1 2 93 84 2

2 ()
93 (2, 0)
84 (1, 0)
2 (0, 0)
"""

tests = int(input())

for _ in range(tests):
    _ = input()
    nums = [int(elem) for elem in input().split()]
    result = []
    for i in range(len(nums)):
        larger = 0
        smaller = 0
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                smaller += 1
            elif nums[i] < nums[j]:
                larger += 1
        
        result.append(str(max(larger, smaller)))

    print(" ".join(result))