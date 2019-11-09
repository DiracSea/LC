class Solution:
    def findNthDigit(self, n: int) -> int:
        # 1~9: 1*9 
        # 10~99: 2*90 
        # 100~999: 3*900 
        # ...
        
        # calculate digits
        base = 9; digits = 1 
        while n - base*digits > 0: 
            n -= base*digits 
            base *= 10 
            digits += 1 
        
        # calculate what number
        idx = n%digits 
        if not idx: 
            idx = digits 
        num = 1 
        for i in range(1, digits): 
            num *= 10 
        
        num += n//digits - 1 if idx == digits else n//digits
        
        # find which digit 
        for i in range(idx, digits): 
            num //= 10 
        return num%10

    # optimization
    def findNthDigit1(self, n: int) -> int:
        n -= 1 
        for digits in range(1, 11): 
            first = 10**(digits - 1) 
            if n < 9*first*digits: 
                return int(str(first + n//digits)[n%digits])
            n -= 9*first*digits 