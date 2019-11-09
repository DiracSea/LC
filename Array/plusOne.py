class Solution:
    def plusOne(self, digits): 
        n = len(digits) 
        flag = 1
        for i, d in enumerate(reversed(digits)): 
            num = d + flag 
            j = n - i - 1 
            if num is not 10: 
                digits[j] = num 
                flag = 0 
            else: 
                digits[j] = 0 
                flag = 1 
        if flag: 
            return [1] + digits 
        return digits 

    def plusOne1(self, digits): 
        digits[-1] += 1
        i = len(digits) - 1
        while i > 0 and digits[i] == 10:
            digits[i-1] += 1
            digits[i] = 0
            i -= 1
        if i == 0 and digits[i] == 10:
            digits[i] = 0
            digits.insert(0, 1)
        
        return digits 

    