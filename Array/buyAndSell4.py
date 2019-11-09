class Solution:
    def maxProfit(self, k: int, prices) -> int:
        n = len(prices) 
        if n == 0:  return 0 
        if k > n/2: return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)) 
        buy = [float("-inf")]*(k+1) 
        buy[0] = 0 
        sell = [0]*(k+1)  
        for p in prices: 
            for i in range(1, k+1): 
                buy[i] = max(buy[i], sell[i-1] - p) 
                sell[i] = max(sell[i], buy[i] + p) 
        return sell[k] 