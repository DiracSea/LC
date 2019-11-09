from functools import reduce 
class Solution:
    def addDigits1(self, num: int) -> int: 
        while num >= 10: 
            num = reduce(lambda x, y: int(x)+int(y), list(str(num))) 
        return num 
    
    def addDigits2(self, num: int) -> int: 
        while num>9:
            num=sum(int(c) for c in str(num))
        return num

    O1 O1
    def addDigits3(self, num: int) -> int: 
        '''
        For base b (decimal case b = 10), the digit root of an integer is:

        dr(n) = 0 if n == 0
        dr(n) = (b-1) if n != 0 and n % (b-1) == 0
        dr(n) = n mod (b-1) if n % (b-1) != 0
        or
        dr(n) = 1 + (n - 1) % 9
        ''' 
        if num == 0: 
            return 0 
        return 1 + (num - 1)%9 