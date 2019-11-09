class Solution:
    # If an optimal product contains a factor f >= 4, 
    # then you can replace it with factors 2 and f-2 without losing optimality, as 2*(f-2) = 2f-4 >= f
    def integerBreak(self, n: int) -> int:
        # 2+2 == 2*2 == 4, in order to get more power, 3 is the best choice
        if n < 4: 
            return 1*(n-1)
    
        mod = n%3 
        if mod == 0: 
            return pow(3, n//3)
        elif mod == 1: 
            return 4*pow(3, n//3 - 1)
        else: 
            return mod*pow(3, n//3)
    
    def integerBreak1(self, n: int) -> int:
        # iterative 
        if n < 4: 
            return n-1
        ans = 1 
        while n > 4: 
            ans *= 3 
            n -= 3 
        return ans*n 

    def integerBreak2(self, n: int) -> int:
        # dp 
        # find the best route 
        if n > 3: n += 1 
        dp = [0]*(n+1) 
        dp[1] = 1 
        
        for i in range(2, n+1): # from 2 to any other nums <= n
            for j in range(1, i): # all past res
                dp[i] = max(dp[i], j*dp[i-j]) 
        
        return dp[-1]