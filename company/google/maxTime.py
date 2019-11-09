class Solution: 
    def maxTime(self, s): 
        res = ''
        h1, h2 = s[0], s[1] 
        m1, m2 = s[3], s[4] 
        q = '?'

        # h1
        if h1 == q: 
            if h2 == q or h2 <= '3': 
                res += '2'
            else: 
                res += '1' 
        else: 
            res += h1 
        
        # h2 
        if h2 == q: 
            if res == "2": 
                res += '3'
            else: 
                res += '9'
        else: 
            res += h2

        res += ':'

        # m1 
        if m1 == q: 
            res += '5'
        else: 
            res += m1

        if m2 == q: 
            res += '9' 
        else: 
            res += m2 

        return res

        