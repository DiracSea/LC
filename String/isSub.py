class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        if not s: 
            return True 
        elif not t: 
            return False 
        elif len(s) > len(t): 
            return False 
        
        d = list(s)
        new_s = "" 
        
        '''
        for idx, value in enumerate(s): 
            d[idx] = value 
            
            # d[i] = d.get(i, 0) + 1 
        '''
        
        # count = 0 
        for idx, value in enumerate(t): 
            if d: 
                if value == d[0]: 
                    new_s += d.pop(0) 
                if new_s == s: 
                    return True 
            else: 
                return False 
        return False 

    # change t
    def isSubsequence1(self, s: str, t: str) -> bool: 
        for ch in s:
            idx = t.find(ch,0)
            if idx == -1:
                return False
            t = t[idx+1:]
        return True

    def isSubsequence2(self, s: str, t: str) -> bool: 

        t = iter(t)
        return all(c in t for c in s)