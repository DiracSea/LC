class Solution:
    def maxProfit(self, prices) -> int:
        # dp 
        # dp[i][0][s] = 0 
        # dp[-1][k][0] = 0 
        # dp[-1][k][1] = -inf 
        # dp[i][k][0] ~ sell/unhold 
        # dp[i][k][1] ~ buy/hold 
        # dp[i][k][s] ~= dp[i-1][k][s] 
        # k = 0, 1, 2 
        # s = 0, 1 
        
        n = len(prices) 
        sell_1 = sell_2 = 0 
        buy_1 = buy_2 = float('-inf') 
        for p in prices: 
            buy_1 = max(buy_1, -p) # dp[i][0][1] - p = -p 
            sell_1 = max(sell_1, buy_1 + p) 
            buy_2 = max(buy_2, sell_1 - p) 
            sell_2 = max(sell_2, buy_2 + p) 
        return sell_2 