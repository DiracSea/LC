class Solution:
    def isUgly(self, num: int) -> bool:
        # math
        return num > 0 and not 2**31*3**19*5**13%num 

    def isUgly1(self, num: int) -> bool:
    
        for p in 2, 3, 5: 
            while num%p == 0 < num: # num% is 0 and num > 0
                num /= p 
        return num == 1

    # brute force
    def isUgly2(self, num: int) -> bool:
        if num <= 0: 
            return False 
        while not num%30: 
            num /= 30 
        while not num%10: 
            num /= 10 
        while not num%15: 
            num /= 15 
            
        while not num%5: 
            num /= 5 
        while not num%3: 
            num /= 3 
        while not num%2: 
            num /= 2 
        
        if num == 1: 
            return True 
        else: 
            return False 