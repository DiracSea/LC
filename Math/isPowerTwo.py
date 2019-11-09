class Solution:
    # math 
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True 
        elif n <= 0: 
            return False 
        elif n < 1: 
            while n < 1: 
                n *= 2 
            return n == 1 
        else: 
            while n > 1: 
                n /= 2 
            return n == 1 

    def isPowerOfTwo1(self, n: int) -> bool:
        # trick
        # bit op
        # 1: 1; 2: 10; 4: 100; 8: 1000
        return n > 0 and not n&(n-1)

    def isPowerOfTwo2(self, n: int) -> bool:
        # iterative 
        if n <= 0: 
            return False 
        while n%2 == 0: 
            n /= 2 
        return n == 1 

    def isPowerOfTwo3(self, n): 
        # recursive
        return i > 0 and (n == 1 or (n%2 == 0 and self.isPowerOfTwo(n/2)))

    def isPowerOfTwo4(self, n): 
        # math 
        return i > 0 and 1073741824 % n == 0

    def isPowerOfTwo5(self, n: int) -> bool:
        # table
        return n in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536,   131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608,16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]
    
    def isPowerOfTwo6(self, n): 
        # bit count 
        return n > 0 and str(bin(n)).count('1') == 1