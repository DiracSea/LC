class Solution:
    def maxProfit(self, prices) -> int: 
        '''
        Simple One Pass 
        1234: 4-1 = 2-1 + 3-2 + 4-3
        1324: 3-1 + 4-2 > 4-1
        1423: 4-1 + 3-2
        draw list figure 
        Greedy Method, split 
        '''
        return sum(max(0, prices[i + 1] - prices[i]) for i in range(len(prices) - 1)) 

    #Peak Valley Approach