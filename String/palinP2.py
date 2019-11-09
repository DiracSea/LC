class Solution:
    def minCut(self, s: str) -> int:

        size = len(s)
        cut = list(range(-1, size))
        for idx in range(1, size):
            for low, high in (idx, idx), (idx - 1, idx):
                while low >= 0 and high < size and s[low] == s[high]:
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low -= 1
                    high += 1
        return cut[-1]
    
    def minCut1(self, s: str) -> int:
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = [x for x in range(-1,len(s))]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]


    # dp
    def minCut2(self, s: str) -> int:
        n = len(s)
        if n < 2: return 0 
        
        # dp[i] means minCut for s[:i] to be cut 
        dp = [i - 1 for i in range(n + 1)]
        
        for i in range(n+1): 
            j = 0
            while i - j >= 0 and i + j < n and s[i + j] == s[i - j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j] + 1)
                j += 1
            j = 1
            while i - j + 1 >= 0 and i + j < n and s[i - j + 1] == s[i + j]:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i - j + 1] + 1)
                j += 1
                    
        return dp[n] 