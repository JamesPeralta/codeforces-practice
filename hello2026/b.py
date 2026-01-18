"""
After 𝑛−𝑘+1
 operations, you will have a sequence of length 𝑘−1
.

Your objective is to maximize the mex
 of the remaining elements.

 The minimum excluded (MEX) of a collection of integers 𝑐1,𝑐2,…,𝑐𝑘
 is defined as the smallest non-negative integer 𝑥
 which does not occur in the collection 𝑐
.

Can it be greedy??

If I have a mex 

Please output the maximum mex
 possible.


 0, 1, 2
 ^

I want to keep the lowest integers in there as much as possible

Do sliding window to find all windows of maximum mex.

Out of all indices choose the largest number and remove it..

For the..
do this 𝑛−𝑘+1

{
 mex: [(l, r)]
}


seen = set()
0 2 1 3
^

0


how do I find mex of each window
Can I do sliding window


1, 2, 3, 0

smallest = 0
"""
from collections import defaultdict

def get_all_mex(nums, k):
    largest_mex = 0
    mex_to_range = defaultdict(list)
    for i in range(len(nums) - k + 1):
        seen = set()
        for j in range(i, i + k):
            seen.add(nums[j])
        
        smallest = 0
        while smallest in seen:
            smallest += 1

        largest_mex = max(largest_mex, smallest)
        mex_to_range[smallest].append((i, i + k))

    largest_elem = 0
    to_delete = 0
    print(mex_to_range)
    for ranges in mex_to_range[largest_mex]:
        for index in range(ranges[0], ranges[1]):
            if nums[index] > largest_elem:
                to_delete = index
                largest_elem =nums[index] 

    print(largest_elem)
    return to_delete


test_cases = int(input())

for i in range(test_cases):
    line = input().split()
    n, k = int(line[0]), int(line[1])
    nums = input().split()
    nums = [int(num) for num in nums]
    for _ in range(n - k):
        to_delete = get_all_mex(nums, k)
        nums.pop(to_delete)
        print("deleting ", to_delete)
        print(nums)
        

    print(nums)

"""
test 0 
1
7 5
0 1 2 4 0 3 1

test 1

1
5 3
0 1 2 1 0
"""