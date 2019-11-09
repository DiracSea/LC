class Solution:
    def lastRemaining(self, n: int) -> int: 
        # f(n)=2(1+n/2-f(n/2))
        return 1 if n == 1 else 2*(1 + n//2 - self.lastRemaining(n//2))
        
    def lastRemaining1(self, n: int) -> int: 
        # recursive
        return self.helper(n, 1) 
    
    def helper(self, n, isLeft): 
        if n == 1: 
            return 1 
        if isLeft: 
            return 2*self.helper(n//2, 0) 
        
        # if from left, [1 2 3 4 5 6] == [2 4 6 8] == 2*[1 2 3 4] 
        elif n%2 == 1: # from right, but length is odd
            return 2*self.helper(n//2, 1) 
        
        # [1 2 3 4 5 6] == [1 3 5] == 2*[1 2 3] - 1
        else: 
            return 2*self.helper(n//2, 1) - 1 

    def lastRemaining2(self, n: int) -> int: 
        # clear 
        left = True 
        # remain = n 
        step = 1 
        head = 1 
        while n > 1: 
            if left or n%2 == 1: 
                head = head + step 
            
            n //= 2 
            step *= 2 
            left = not left 
            
        return head 