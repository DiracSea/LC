class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: 
            return ""
        l = r = 0 # pointer 
        window = ""
        length, l1, r1 = float("inf"), 0, 0 # ans =
        
        d = __import__("collections").Counter(t) # count all char in t 
        req = len(d) 
        
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        win = {} 
        
        while r < len(s): 
            ch = s[r] 
            win[ch] = win.get(ch, 0) + 1 # check if ch exists, and count
            
            if ch in d and win[ch] == d[ch]: 
                formed += 1 
            
            while l <= r and formed == req: 
                ch = s[l] 
                
                if r - l + 1 < length: 
                    l1 = l; r1 = r
                    length = r1 - l1 + 1 
                
                win[ch] -= 1 
                if ch in d and win[ch] < d[ch]: 
                    formed -= 1
                
                l += 1 
            
            r += 1 
        return "" if length == float("inf") else s[l1 : r1 + 1]


    # optimize poiner
    def minWindow1(self, s: str, t: str) -> str:
        if not t or not s: 
            return ""
        l = r = 0 # pointer 
        window = ""
        length, l1, r1 = float("inf"), 0, 0 # ans =
        
        d = __import__("collections").Counter(t) # count all char in t 
        req = len(d) 
        
        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered = [] 
        for i, ch in enumerate(s): 
            if ch in d: 
                filtered.append((i, ch))
        
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        win = {} 
        
        while r < len(filtered): 
            ch = filtered[r][1] 
            win[ch] = win.get(ch, 0) + 1 # check if ch exists, and count
            
            if ch in d and win[ch] == d[ch]: 
                formed += 1 
            
            while l <= r and formed == req: 
                ch = filtered[l][1] 
                
                end = filtered[r][0]
                start = filtered[l][0] 
                if end - start + 1 < length: 
                    length = end - start + 1 
                    l1 = start 
                    r1 = end 
                
                win[ch] -= 1 
                if ch in d and win[ch] < d[ch]: 
                    formed -= 1
                
                l += 1 
            
            r += 1 
        return "" if length == float("inf") else s[l1 : r1 + 1]
