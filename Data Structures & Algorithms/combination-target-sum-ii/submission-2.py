class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []

        def dfs(i: int, total: int):

            if total == target:
                res.append(sol.copy())
                return

            if i >= len(nums) or target < total:
                return

            sol.append(nums[i])
            dfs(i + 1, total + nums[i])
            sol.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, total)
           

        dfs(0, 0)
        return res
            