class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # newton 
        r = num 
        while r*r > num: 
            r = (r + num/r)//2 # >> 1
        return True if r*r == num else False # return  r*r == num 

    def isPerfectSquare1(self, num: int) -> bool:
        # binary 
        if num == 1: 
            return True 
        low, high = 1, num>>1 
        while low <= high: 
            mid = (low + high)>>1 
            sqr = mid*mid 
            if sqr == num: 
                return True 
            elif sqr > num: 
                high = mid - 1 
            else: 
                low = mid + 1 
        return high*high == num  
