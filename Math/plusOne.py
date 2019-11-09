class Solution:
    def plusOne(self, digits): 
        if digits[-1] != 9: 
            digits[-1] += 1 
            return digits 
        else: 
            one = False 
            for i in range(len(digits)-1, -1, -1): 
                if digits[i] == 9: 
                    digits[i] = 0 
                else: 
                    digits[i] += 1 # others remain the same 
                    one = True 
                    break 
            
            if not one: # add one 
                digits = [1] + digits
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