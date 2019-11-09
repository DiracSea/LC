class Solution:
    def myPow(self, x: float, n: int) -> float: 
        # recursive 
        # between odd and even 
        if not n: 
            return 1 
        if n < 0: 
            return 1/self.myPow(x, -n) 
        if n%2: # if odd 
            return x*self.myPow(x, n-1) 
        return self.myPow(x*x, n/2) 

    def myPow1(self, x: float, n: int) -> float: 
        # iterative 
        if n < 0: 
            x = 1/x 
            n = -n 
        pow = 1 
        while n: 
            if n%2: # or n&1 odd 
                pow *= x 
            x *= x 
            n >>= 1 # n //= 2 
        return pow 

    def myPow(self, x: float, n: int,r=1) -> float:
        # recursive 
        x, n = n < 0 and 1 / x or x, abs(n)
        return self.myPow(x * x, n // 2, r * (not n % 2 or x)) if n else r

    def myPow2(self, x: float, n: int) -> float: 
        if n == 0: 
            return 1 
        if x == 1 or x == 0: 
            return x 
        if x >= -2147483648 and x <= 2147483647: 
            return x**n 
        elif x < -2147483648: 
            return -2147483648 
        else: 
            return 2147483647