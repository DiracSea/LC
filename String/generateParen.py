class Solution:
    def generateParenthesis(self, n: int):
        ans = [] 
        def backtrack(s = '', l = 0, r = 0): 
            if len(s) == 2*n: 
                ans.append(s) 
                return 
            if l < n: 
                backtrack(s+'(', l+1, r) 
            if r < l: 
                backtrack(s+')', l, r+1) 
            
        backtrack() 
        return ans 

    def generateParenthesis1(self, n: int):
        # iterate 
        dp = {i:[] for i in range(n+1)} 
        dp[0] = [''] 
        dp[1] = ['()'] 
        dp[2] = ['()()', '(())'] 
        
        if n <= 2: 
            return dp[n] 
        
        for i in range(3, n+1): 
            for j in range(i): 
                for c1 in dp[j]: 
                    for c2 in dp[i-j-1]: 
                        dp[i].append('('+c1+')'+c2) 
                        
        return dp[n]