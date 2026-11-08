class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        dp = [0] * len(cost)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return dp[-1]