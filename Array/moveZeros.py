class Solution: 
    # 1 count zero number
    # 2 move all non-zero number 
    # 3 add zero in the end 
    # very bad On On
    def moveZeroes(self, A) -> None:

        # optimal 
        n = len(A) 
        z = 0 
        for i in A: 
            z += (i == 0) 
        ans = [] 
        for i in A: 
            if i is not 0: 
                ans.append(i) 
        while z > 0: 
            ans.append(0) 
            z -= 1 
        for i in range(0, A): 
            A[i] = ans[i]
    
    def moveZeroes1(self, A) -> None:

        # 
        last = 0 
        # If the current element is not 0, then we need to
        # append it just in front of last non 0 element we found. 
        for i in range(0, len(A)): 
            if A[i] is not 0: 
                A[last] = A[i] 
                last += 1 
        
        for i in range(last, len(A)): 
            A[i] = 0 
    
    
