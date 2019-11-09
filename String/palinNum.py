class Solution:
    def isPalindrome(self, x: int) -> bool:
        # reverse and compare 
        def reverse(x): 
            rev = 0 
            while x != 0: 
                offset = x%10 
                x //= 10 
                if rev > __import__('sys').maxsize//10: 
                    return 0 
                rev = rev*10 + offset 
                
            return rev 
        if x < 0: 
            return False 
        rev = reverse(x) 
        return rev == x 
    
    def isPalindrome1(self, x: int) -> bool:
        # str
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x: int) -> bool:
        # compare half right and left 
        if x < 0: 
            return False 
        elif x == 0: 
            return True 
        digit = int(__import__('math').log(x, 10) + 1) # all digits
        revert = 0 
        offset = 0 
        
        for i in range(digit//2): 
            offset = x%10 
            revert = revert*10 + offset 
            x //= 10 
            
        if digit%2 == 0 and x == revert: 
            return True 
        
        if digit%2 == 1 and x//10 == revert: 
            return True
        
        return False 