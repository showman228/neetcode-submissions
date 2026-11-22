from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                count += 1
        return count