class Solution:
##############################################
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: 
            return 0 
        ''' 
        symbol = (dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0) - (dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0) 
        if dividend < 0: 
            dividend = -dividend 
        if divisor < 0: 
            divisor = -divisor 
        ''' 
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor: 
            tmp, i = divisor, 1 
            while dividend >= tmp: 
                dividend -= tmp 
                res += i 
                i <<= 1 #   *2
                tmp <<= 1 # *2
        if not positive: 
            res = -res 
        return min(max(-2147483648, res), 2147483647) 