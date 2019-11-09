class Solution:
    def integerReplacement(self, n: int) -> int:
        # bit manipulation
        # if n+1 > n-1 - else +
        c = 0 
        while n > 1: 
            num1 = str(bin(n + 1)).count('1')
            num2 = str(bin(n - 1)).count('1')
            if not n&1: # n&2 == 0
                n >>= 1 # n //= 2
            elif n == 3 or num1 > num2: 
                n -= 1 
            else: 
                n += 1 
            c += 1 
        return c

    ##############
    cache = {1:0}
    def integerReplacement1(self, n: int) -> int:
        # recursive 
        if n in self.cache: 
            return self.cache[n] 
        
        if n&1 == 0: 
            ans = self.integerReplacement1(n//2) + 1 
        else: 
            ans = min(self.integerReplacement1(n-1), self.integerReplacement1(n+1)+1) 
        self.cache[n] = ans 
        return ans