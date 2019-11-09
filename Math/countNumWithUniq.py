class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # combiantion
        '''
        f0 = 1
        f1 = 10 
        f2 = f1 + 9*9 (first is not 0, second is not first)
        f3 = f2 + 9*9*8 (1st is not 0, 2nd is not 1st, 3rd is not 1 or 2)
        f11 = f10 + 9*9*8*7*.*0
        '''
        if not n: 
            return 1 
        ans = 10
        base = 9 # 1st is not 0 
        for i in range(2, min(11, n+1)): 
            base *= (11 - i)
            ans += base 
        return ans 

    #####################
    def countNumbersWithUniqueDigits1(self, n: int) -> int:
        # backtracking 
        c = 0 
        if not n: return 1 
        flags = [False]*10 
        c += self.countNumbersWithUniqueDigits(n-1) 
        for i in range(1,10): 
            flags[i] = True 
            c += self.search(n-1, flags) 
            flags[i] = False 
        return c
            
    def search(self, n, flags): 
        if not n: 
            return 1 
        c = 0 
        for i in range(10): 
            if not flags[i]: 
                flags[i] = True 
                c += self.search(n-1, flags) 
                flags[i] = False 
        
        return c