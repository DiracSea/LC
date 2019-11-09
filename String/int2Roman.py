class Solution:
    def intToRoman(self, num: int) -> str:
        # database 
        # because 1 - 4000
        M = ["", "M", "MM", "MMM"] 
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"] 
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"] 
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"] 
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10] 
    
    def intToRoman1(self, num: int) -> str:
        # brute force
        res = "" 
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
        i = 0 
        while num > 0: 
            while num >= value[i]: 
                num -= value[i] 
                res += roman[i]  
            i += 1 
        return res 