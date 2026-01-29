# Pattern: Gather–rotate–scatter — collect all non-negative elements and their indices, rotate the values by k (mod length), write back at original indices
class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        non_negative = []
        missing_index = []
        for index, num in enumerate(nums):
            if num >= 0:
                non_negative.append(num)
                missing_index.append(index)

        new_index = {}
        for index, elem in enumerate(non_negative):
            i = (index - k) % len(non_negative)
            print(elem - k, i)
            new_index[i] = elem

        for index, elem in enumerate(missing_index):
            nums[elem] = new_index[index]
        return nums
        # [1, 3].. Just rotate the postive ints and keep all negatives in place

        






"""
- find all non negative elements and their index..
- []

"""














        