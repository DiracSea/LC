class Solution: 
    # two scan: forward and backward On On
    def candy(self, ratings) -> int: 
        n = len(ratings) 
        if n < 2: return n 
        nums = [1]*n 
        for i in range(1, n): 
            if ratings[i] > ratings[i - 1]: 
                nums[i] = nums[i - 1] + 1 
        
        for i in range(1, n): 
            j = n - i 
            if ratings[j - 1] > ratings[j]: 
                nums[j - 1] = max(nums[j - 1], nums[j] + 1) 
                
        return sum(nums)


    # peak and down On O1
    def candy1(self, ratings) -> int: 
        n = len(ratings) 
        if n < 2: return n 
        res = 1 
        up, down, peak = 0, 0, 0 
        for i in range(1, n): 
            if ratings[i - 1] < ratings[i]: 
                up += 1 
                peak = up  
                down = 0 
                res += 1 + up 
            elif ratings[i - 1] == ratings[i]: 
                peak = down = up = 0 
                res += 1 
            else: 
                up = 0 
                down += 1 
                res += 1 + down + (-1 if peak >= down else 0) 
        
        return res 