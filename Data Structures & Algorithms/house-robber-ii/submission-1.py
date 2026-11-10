class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        sp = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if sp[i][flag] != -1:
                return sp[i][flag]
            
            sp[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag or (i == 0)))

            return sp[i][flag]
        
        return max(dfs(0, True), dfs(1, False))

    