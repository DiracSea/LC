class Solution:
    def isHappy(self, n: int) -> bool:
        # cycle
        s = set() 
        while n > 1: 
            n = sum([int(i)**2 for i in str(n)])
            if n in s: 
                return False 
            else: 
                s.add(n) 
        return True

    def isHappy1(self, n: int) -> bool:
        # O1 space 
        def cal(n): 
            x = n 
            s = 0 
            while x > 0: 
                s = s + (x%10)**2 
                x = x//10 
            return s
        
        x = n 
        y = n 
        while x > 1: 
            x = cal(x) 
            
            if x == 1: return True
            
            y = cal(cal(y)) 
            
            if y == 1: return True 
            
            if x == y: return False 
        return True 

    def isHappy2(self, n: int) -> bool:
        # math
        while n > 1: 
            n = sum([int(i)**2 for i in str(n)])
            if n == 1: 
                return True
            elif n == 89: 
                return False
        return True