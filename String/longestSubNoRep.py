class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 
        if s == " ": 
            return 1  
        elif s == "": 
            return 0 
        
        win = [] 
        length = 0 
        p = 0 
        
        while p < len(s): 
            if s[p] not in win: 
                win.append(s[p]) 
                length += 1 
                
            else: 
                while s[p] in win: 
                    win = win[1:] 
                    length -= 1 
                win.append(s[p]) 
                length += 1 
                
            
            p += 1 
            longest = max(longest, length) 
        return longest 


    def lengthOfLongestSubstring1(self, s: str) -> int:
        d = {} 
        maxL = start = 0 
        for idx, ch in enumerate(s): 
            if ch in d: 
                newS = d[ch] + 1  # give a new start point
                start = max(start, newS)
                    
            num = idx - start + 1 # the interval 
                
            maxL = max(maxL, num) 
            d[ch] = idx  
        return maxL 