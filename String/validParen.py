class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        stack = [] 
        d = {']':'[', '}':'{', ')':'('} 
        
        for ch in s: 
            if ch in d.values(): 
                stack.append(ch) 
            elif ch in d.keys(): 
                if stack == [] or d[ch] != stack.pop(): # must pair 
                    return False 
            else: 
                return False 
            
        return stack == [] # stack must be empty 

    # optimization
    def isValid1(self, s: str) -> bool:
        # stack 
        stack = ['#'] 
        d = {']':'[', '}':'{', ')':'('} 
        
        for ch in s: 
            if ch in d: 
                if stack.pop() != d[ch]: 
                    return False 
            else: 
                stack.append(ch)
            
        return len(stack) == 1 

    # replace
    def isValid2(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False