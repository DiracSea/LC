class Solution: 
    # brute force 
    # TLE 

    def maxRotateFunction(self, A) -> int:
        '''
        1 
        F(k)   = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
        F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
               = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
               
        2 
        F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
                      = (Bk[0] + ... + Bk[n-1]) - nBk[0]
                      = sum - nBk[0] 
                      
        3 
        F(k) = F(k-1) + sum - nBk[0]
        
        4 
        k   Bk[0]
        0   A[0]
        1   A[n-1]
        2   A[n-2]
        ''' 
        n = len(A)
        total = sum(A) 
        F = 0 
        for idx, value in enumerate(A): # F0
            F += idx*value 
            
        res = F
        
        for i in range(1, n): 
            F += total - n*A[n-i]
            res = max(res, F)

        # or 
        '''
        while A: 
            F += total - n*A.pop()
            res = max(res, F)
        '''
        return res 
        