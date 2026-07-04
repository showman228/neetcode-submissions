class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_prices = prices[0]
        profit = 0

        for p in range(1, len(prices)):
            if buy_prices > prices[p]:
                buy_prices = prices[p]
            
            profit = max(profit, prices[p] - buy_prices)
        
        return profit