class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and not num&(num-1) and num&1431655765 == num

    def isPowerOfFour1(self, num: int) -> bool:
        # bit count 
        if num > 0: 
            b = str(bin(num))[2:] 
            if b.count('1') == 1: 
                return not b.count('0')%2 
        return False 

        # return num > 0 and str(bin(num)).count('1') == 1 and str(bin(num)).count('0')%2