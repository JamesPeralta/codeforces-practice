from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        segs = defaultdict(set)
        left, last_elem = 0, nums[0]
        """
        1, 2, 2, 3,
        ^
        """
        # size = 0
        for right in range(len(nums)):
            curr_elem = nums[right]

            if curr_elem != nums[left]:
                should_add = False
                for index in range(left, right):
                    if target[index] != nums[index]:
                        should_add = True
                        break
                # print(should_add, left, right)
                if should_add:
                    segs[nums[left]].add(right - left)

            while curr_elem != nums[left]:
                left += 1
        
        should_add = False
        for index in range(left, len(nums)):
            if target[index] != nums[index]:
                should_add = True
                break
        if should_add:
            segs[curr_elem].add(len(nums) - left)

        # print(segs)
        result = 0
        # for elem in segs:
        #     result += len(segs[elem])
        return len(segs)
        # print(segs)
"""
{
 num: set(sizes of segs)
}


for each segment - filter out segments out ones that already meet target

Hashmap of alll segments the same size


Where I went wrong:
- I misread this -> Find all maximal contiguous segments where nums[i] == x (a segment is maximal if it cannot be extended to the left or right while keeping all values equal to x).. 








"""