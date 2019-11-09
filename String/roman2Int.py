class Solution:
    # roman specility
    # 1 minus has only previous one IV, IX 
    # 
    def romanToInt(self, s: str) -> int: 
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0 
        prev = 0 
        for i in s[::-1]:
            cur = roman[i] 
            if prev > cur: 
                num -= cur # minus only have one space: IV, VI, VII, VIII, IX
            else: 
                num += cur 
            prev = cur 
        return num 

    def romanToInt1(self, s: str) -> int: 
        # replace minus to plus: IV to IIII etc. 
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0 
        s = s.replace("IV", "IIII").replace("IX", "VIIII") # 4, 9
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX") # 40 90
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC") # 400 900
        for i in s:
            num += roman[i] 
        return num 