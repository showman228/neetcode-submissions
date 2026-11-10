class Solution:
    def rob(self, nums: List[int]) -> int:
        sp = [-1] * len(nums)

        def dfs(i: int):
            if i >= len(nums):
                return 0
            
            sp[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])
            return sp[i]

        return max(dfs(0), dfs(1))      
    