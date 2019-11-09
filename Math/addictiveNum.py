class Solution:
    def isAdditiveNumber(self, num: str) -> bool: 
        # two pointers and recursive
        n = len(num) 
        
        # first num A 
        for i in range(1, (n+1)//2): 
            # A cannot start with 0 if it is more than 1 
            if num[0] == '0' and i > 1: 
                break 
            
            # sencond num B 
            # n - j >= j - i -> n + i >= 2*j and n - i >= j
            for j in range(i + 1, min((n+i)//2, n-i) + 1): 
                # B cannot start with 0 if it is more than 1 
                if num[i] == '0' and j - i > 1: 
                    break
                num1 = int(num[0:i]) # A
                num2 = int(num[i:j]) # B
                substr = num[j:] # remain string 
                
                if self.isAddictive(substr, num1, num2): 
                    return True 
                    
        return False 
    
    def isAddictive(self, substr, num1, num2): 
        if substr == "": # reach the end 
            return True
        
        total = num1 + num2 
        s = str(total) 
        
        if not substr[:len(s)] == s: # C not in substr
            return False 
        
        return self.isAddictive(substr[len(s):], num2, total) # recursive add 

    def isAdditiveNumber1(self, s: str) -> bool: 
        # DFS 
        n = len(s) 
        for i in range(1, n): 
            for j in range(i+1, n): 
                a = self.parse(s[:i]) 
                b = self.parse(s[i:j]) 
                if a == -1 or b == -1: 
                    continue 
                if self.dfs(s[j:], a, b): 
                    return True 
        return False 
                
    def dfs(self, s, a, b): 
        if len(s) == 0: return True 
        
        for i in range(1, len(s) + 1): 
            c = self.parse(s[:i]) 
            if c == -1: continue 
            if c-a == b and self.dfs(s[i:], b, c): return True
    
    # break 
    def parse(self, s): 
        # s is more than 1 but start with 0 
        if len(s) > 1 and s[0] == '0': return -1 
        return int(s) 
        