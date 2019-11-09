class Solution:
    # front add 
    def shortestPalindrome(self, s: str) -> str: 
        if not s or len(s) == 1 or s == s[::-1]: 
            return s 
        r = -1 
        n = len(s) 
        front = ''
        while r > -n: 
            front = front + s[r] 
            tmp = front + s
            if tmp == tmp[::-1]: 
                return tmp 
            r -= 1 
        return s 

    def shortestPalindrome1(self, s: str) -> str:
        # recursion
        if not s or len(s) == 1 or s == s[::-1]: 
            return s 
        j = 0 
        for i in reversed(range(len(s))): 
            if s[i] == s[j]: 
                j += 1 # find palin center
        return s[j:][::-1] + self.shortestPalindrome(s[:j-len(s)]) + s[j-len(s):]


    def shortestPalindrome2(self, s: str) -> str:
        # kmp 
        # s + # + reversed(s) 
        # find the longest palindrome substring starts from index 0 
        ss = s + '#' + s[::-1] 
        kmp = [-1] + [0]*len(ss) 
        l, r = -1, 0 # l pre; r post 
        '''
        while r < len(ss): 
            while l >= 0 and ss[l] != ss[r]: 
                l = kmp[l] 
            l, r = l + 1, r + 1 
            kmp[r] = l 
        '''
        
        while r < len(ss): 
            if l == -1 or ss[l] == ss[r]: 
                l += 1 
                r += 1 
                kmp[r] = l 
            else: 
                l = kmp[l] 
                
        return s[kmp[-1]:][::-1] + s 