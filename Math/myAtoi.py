class Solution:
    def myAtoi(self, str: str) -> int: 
        # symbol = '+-' 
        symbol = 1 
        # digit = '0123456789' 
        rev = 0
        
        str = str.strip() 
        
        if not str: 
            return 0 
        elif str[0] == '+': 
            symbol = 1  
        elif str[0] == '-': 
            symbol = -1 
        elif str[0].isdigit(): 
             rev += int(str[0])
        else: 
            return 0 
        
        for i in str[1:]: 
            if i.isdigit(): 
                rev = rev*10 + int(i) 
            else: 
                break 
        ans = rev*symbol 
        if ans < -2**31: 
            ans = -2**31 
        elif ans > 2**31-1: 
            ans = 2**31-1
        return ans