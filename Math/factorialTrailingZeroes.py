class Solution:
    def trailingZeroes(self, n: int) -> int:
        # trailing zero so not include middle zero 
        # trailing zero must be 10 = 2*5 
        # 2 is enough so calculate num of 5 
        # we encounter a multiple of 5 every 5 numbers
        # 10 = 2*5
        # 25 = 5*5 -> 5 10 15 20 25 = 1+1+1+1+2 = 5's 5 1's 25
        # count = n/5 + n/25 + n/125 + ... + 0
        # f(n)=n/5+f(n/5)
        return 0 if not n else n//5 + self.trailingZeroes(n//5)

    def trailingZeroes1(self, n: int) -> int:
        # f(n)=n/5+f(n/5) 
        c, i = 0, 5 
        while n >= i: 
            c += n//i 
            i *= 5 
        return c