class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # math 
        return n > 0 == 3**19%n

    def isPowerOfThree1(self, n: int) -> bool:
        # iterative 
        if n <= 0: 
            return False 
        while n%3 == 0: 
            n /= 3 
        return n == 1 