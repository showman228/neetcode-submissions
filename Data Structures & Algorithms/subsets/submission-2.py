class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def dfs(i: int):

            if i >= len(nums):
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            dfs(i + 1)
            sol.pop()
            dfs(i + 1)

        dfs(0)
        return res