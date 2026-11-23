from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) % 2:
            return False
        
        total_sum_nums = sum(nums)
        @lru_cache(None)
        def dfs(i: int, target: int):

            if i >= len(nums):
                return target == 0

            if target < 0: return False

            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

            
        return dfs(0, total_sum_nums // 2)