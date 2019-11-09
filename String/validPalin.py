class Solution:
    def isPalindrome(self, s: str) -> bool:
        isValid = "" 
        for i in s: 
            if i >= 'a' and i <= 'z' or i >= '0' and i <= '9': 
                isValid += i 
            elif i >= 'A' and i <= 'Z': 
                isValid += chr(ord(i) + ord('a') - ord('A')) 
        
        for i in range(len(isValid)//2): 
            if isValid[i] != isValid[len(isValid) - i - 1]: 
                return False 
        return True 


    def isPalindrome1(self, s: str) -> bool:
        ignore_chars = ',./<>?;\':"[]\{}|`~!@#$%^&*()-=_+ '
        for char in ignore_chars:
            if char in s:
                s = s.replace(char,'')
        return s.lower() == s.lower()[::-1] 

    # On O1
    def isPalindrome2(self, s: str) -> bool: 
        l, r = 0, len(s) - 1 
        while l < r: 
            while l < r and not s[l].isalnum(): 
                l += 1 
            while l < r and not s[r].isalnum(): 
                r -= 1 
            if s[l].lower() != s[r].lower(): 
                return False
            l += 1; r -= 1 
        return True


    # bad 
    def isPalindrome0(self, s: str) -> bool: 
        for i in s: 
            if not (i >= 'a' and i <= 'z' or i >= '0' and i <= '9' or i >= 'A' and i <= 'Z'): 
                s = s.replace(i,'')
        
        return s.lower() == s.lower()[::-1]