class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices) 
        sell_0, sell = 0, 0 
        buy = float("-inf") 
        
        for p in prices: 
            tmp = sell 
            sell = max(sell, buy + p) 
            buy = max(buy, sell_0 - p) 
            sell_0 = tmp 
            
        return sell 