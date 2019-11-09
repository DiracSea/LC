class Solution:
    # dp 
    def longestValidParentheses(self, s: str) -> int: 
        long = 0 
        dp = [0]*len(s) 
        
        for i in range(1,len(s)): 
            if s[i] == ')': 
                if s[i - 1] == '(': 
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2 
                
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(': 
                    dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if (i - dp[i-1]) >= 2 else 0) + 2 
                
                long = max(long, dp[i]) 
        return long 


    def longestValidParentheses1(self, s: str) -> int: 
        # stack 
        stack = [0] 
        long = 0 
        
        for ch in s: 
            if ch == '(': 
                stack.append(0) 
            else: 
                if len(stack) > 1: 
                    val = stack.pop() 
                    stack[-1] += val + 2 
                    long = max(long, stack[-1]) 
                else: 
                    stack = [0] 
        
        return long 

    # stack O1
    def longestValidParentheses2(self, s: str) -> int: 
        l, r, long = 0, 0, 0 
        for i in range(len(s)): 
            if s[i] == '(': 
                l += 1 
            else: 
                r += 1 
            
            if l == r: 
                long = max(long, 2*r) 
            elif r >= l: 
                l = r = 0 
            
        l = r = 0 
        for i in range(len(s) - 1, -1, -1): 
            if s[i] == '(': 
                l += 1 
            else: 
                r += 1 
        
            if l == r: 
                long = max(long, 2*l) 
            elif l >= r: 
                l = r = 0
        
        return long 

    # TLE 
    # brute force
    def longestValidParentheses3(self, s: str) -> int: 
        if len(s) < 2: 
            return 0 
        
        def isVal(l, r): 
            stack = ['#'] 
            for ch in s[l:r]: 
                if ch == ')': 
                    if stack.pop() != '(': 
                        return False 
                else: 
                    stack.append(ch) 
            return len(stack) == 1 
        
        # l = 0; r = 2
        longest = 0 
        for r in range(1, len(s)): 
            for l in range(r): 
                if (r - l + 1)%2 == 0: 
                    if isVal(l, r+1): 
                        longest = max(r - l + 1, longest)
        return longest 