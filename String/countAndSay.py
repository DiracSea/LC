class Solution:
    def countAndSay(self, n: int) -> str:
        # cur 1 -> 1 
        # cur 2 -> 12(oneone,onetwo) -> 112
        # cur 11 -> 21(onetwooneone) -> 1211
        # cur 22 -> 22 -> 22
        s = "1" 
        if n == 1: 
            return s
        i = 1   
        while i < n:
            mul = 1
            l = ""
            p = s[0] 
            for j in s[1:]: 
                if p == j: 
                    mul += 1 
                else: 
                    l += str(mul) + p
                    p = j 
                    mul = 1 
            l += str(mul) + p
            s = l
            i += 1 
        return s 