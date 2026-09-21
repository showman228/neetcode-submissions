class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyPrice = prices[0];
        int profit = 0;

        for (int p = 1; p < prices.size(); p++) {
            if (buyPrice > prices[p]) {
                buyPrice = prices[p];
            }

            profit = max(profit, prices[p] - buyPrice);
        }
        
        return profit;
    }
};
