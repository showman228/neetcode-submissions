class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(j: int, cur: List[int], total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return

            for j in range(j, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        

        dfs(0, [], 0)
        return res
