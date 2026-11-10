
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sp = [-1] * len(cost)

        def dfs(i: int):
            if i >= len(cost):
                return 0
            if sp[i] != -1:
                return sp[i]
            sp[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return sp[i]
        
        return min(dfs(0), dfs(1))

