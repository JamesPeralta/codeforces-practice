# Pattern: Sliding window (two pointers) + hash map — expand right, shrink left when sum >= k, track distinct sum via frequency map
from collections import defaultdict
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        count = 0
        unique_elems = defaultdict(int)
        
        left, right = 0, 0
        result = float("inf")
        while right < len(nums):
            unique_elems[nums[right]] += 1
            if unique_elems[nums[right]] == 1:
                count += nums[right]
        
            while left < right and count >= k:
                result = min(result, (right - left) + 1)
                unique_elems[nums[left]] -= 1
                if unique_elems[nums[left]] == 0:
                    count -= nums[left]
                left += 1
                # print(left, right)
                # print(count, unique_elems)
            
            # print(left, right)
            # print(count, unique_elems)
            if count >= k:
                result = min(result, (right - left) + 1)
            right += 1
        
        return -1 if result == float("inf") else result 