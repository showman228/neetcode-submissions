class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(i: int, total: int):

            if total == target:
                res.append(path[:])
                return
            
            if total > target or i >= len(nums):
                return

            path.append(nums[i])
            backtrack(i, total + nums[i])
            path.pop()
            backtrack(i + 1, total)


        backtrack(0, 0)
        return res