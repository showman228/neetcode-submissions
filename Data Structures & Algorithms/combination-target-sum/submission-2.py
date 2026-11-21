class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []

        def dfs(i: int, total):
            if total == target:
                res.append(sol.copy())
                return 

            if total > target or i >= len(nums):
                return
            
            sol.append(nums[i])
            dfs(i, total + nums[i])
            sol.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res