class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            seen = set()
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                seen.add(nums[j])
                if curr in seen:
                    result += 1
                
        return result


"""
[-1,1,0]
 l
    r

[5,0,-2,-3]

"""