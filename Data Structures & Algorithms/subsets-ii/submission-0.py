class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(i: int):

            if i == len(nums):
                res.append(path[:])
                return
            

            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            dfs(i + 1)

        dfs(0)
        return res