class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)


    # binary search 
    def mySqrt1(self, x: int) -> int:
        if x == 1: 
            return 1 
        low, high = 1, x//2 
        while low <= high: 
            mid = low + (high - low)//2 
            sqr = mid*mid 
            if sqr == x: 
                return mid 
            elif sqr > x: 
                high = mid - 1 
            else: 
                low = mid + 1 
        return high 

    # newton 插值
    def mySqrt2(self, x): 
        r = x 
        while r*r > x: 
            r = (r + x/r) // 2 
        return r 