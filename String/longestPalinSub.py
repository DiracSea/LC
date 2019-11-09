class Solution:
    def longestPalindrome(self, s: str) -> str:
        # center expand 
        res = ""
        for i in range(len(s)):
            # res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
            
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    
    
    def longestPalindrome1(self, s: str) -> str:
        # dp
        n = len(s) 
        res = "" 
        dp = [[0]*n for i in range(n)] 
        
        for i in range(n-1, -1, -1): 
            for j in range(i, n): 
                dp[i][j] = s[i] == s[j] and (j-i < 3 or dp[i+1][j-1]) 
                
                if dp[i][j] and (res == "" or j-i+1 > len(res)): 
                    res = s[i:j+1]
        return res 

    # On 
    def longestPalindrome2(self, s: str) -> str:
        if len(s)==0:
        	return ""
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]