class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        decreasing = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                break

            decreasing += 1
        return len(nums) - decreasing


"""
[1,-1,2,3,3,4,5]

longest strictly decreasing
"""