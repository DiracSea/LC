class Solution:
    # On On two pointers
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: 
            return True 
        
        l = 0; r = len(s) - 1
        # flag = 0
        while l < r: 
            if s[l] != s[r]: 
                one, two = s[l:r], s[l + 1:r + 1] # remove left or right
                return one == one[::-1] or two == two[::-1]
            l += 1 
            r -= 1 
        return True 

    # 
    def validPalindrome1(self, s: str) -> bool:
        if s == s[::-1]: 
            return True 
        
        for i in range(len(s)-1): 
            if s[i] != s[-i-1]: 
                return s[i:-i-2] == s[i+1:-i-1][::-1] or s[i+1: -i-1] == s[i+2: len(s)-i][::-1]
        return False 
