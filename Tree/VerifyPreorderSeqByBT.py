class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # '#' occupy one slot 
        # number occupy one but create two 
        if preorder == '#': return True 
        
        p = preorder.split(',') 
        n = len(p) 
        
        if (n-1)&1: return False 
        
        a = p.count('#')
        if 2*a - n != 1: return False 
        
        slot = 1 
        for node in p: 
            
            if slot <= 0: # over #
                return False
            
            if node == '#': 
                slot -= 1 
            
            else: # 2-1 = 1
                slot += 1 
                
        return slot == 0

    def isValidSerialization1(self, preorder: str) -> bool:
        # dp
        if preorder == '#' or not preorder: return True 
        
        p = preorder.split(',') 
        n = len(p) 
        
        if (n-1)&1: return False 
        
        a = p.count('#')
        if 2*a - n != 1: return False 
        
        stack = [[p[0], 2]]
        
        for idx in range(1, len(p)): 
            if not stack: return False 
            val = p[idx] 
            if val == '#': 
                if stack: 
                    stack[-1][1] -= 1 
                else: 
                    return False 
                while stack and stack[-1][1] == 0: 
                    stack.pop() 
                    if stack: 
                        stack[-1][1] -= 1 
            else: 
                stack.append([val, 2]) 
        
        return not stack

    def isValidSerialization2(self, preorder: str) -> bool:
        # replace full node
        if not preorder: return False 
        preorder = preorder.split(',') 
        preorder = ['#' if ch == '#' else '0' for ch in preorder] 
        preorder = ''.join(preorder) 
        
        n = len(preorder) 
        length = n+1 
        while n < length: 
            length = n 
            preorder = preorder.replace('0##', '#')
            n = len(preorder)
        
        return preorder == '#'