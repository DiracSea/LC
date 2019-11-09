class Solution:
    # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen
    def maxProfit(self, prices) -> int: 
        max_price = 0 
        buy = float("inf") 
        sell = 0 
        
        for i in prices:  
            gap = i - buy 
            if gap > max_price:
                max_price = gap 
            elif gap < 0: 
                buy = i 
            
        return max_price