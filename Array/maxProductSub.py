class Solution: 
    # 0 divide list 
    # negative num should be counted
    def maxProduct(self, nums) -> int: 
        # time ex
        mi = float("-inf") 
        p = 1 
        p0 = p 
        neg = 0 
        neg0 = neg
        j = 0
        for i in range(0, len(nums)): 
            
            if nums[i] is not 0: 
                p *= nums[i] 
                if nums[i] < 0: 
                    neg += 1 
                mi = max(mi, p)
            else: 
                if mi < 0: mi = 0 
                p = 1 
                neg = 0 
                j = i + 1 
            
            if p < 0 and neg > 0: 
                p0 = p # -12 
                neg0 = neg # 1
                j0 = j # 0
                
                while neg0 >= 0 and j0 < i:                       
                    p0 //= nums[j0]  
                    mi = max(mi, p0) 
                    j0 += 1 
                    if nums[j0] < 0: 
                        neg0 -= 1     
        return mi


    def maxProduct1(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

    def maxProduct2(self, A): 
        r = A[0] 
        # imin/imax stores the min/max product of sub
        imax = imin = r 
        for i in range(1, len(A)): 
            # multiply negative make max smaller
            if A[i] < 0: 
                tmp = imax 
                imax = imin 
                imin = tmp 
            imax = max(A[i], imax*A[i]) 
            imin = min(A[i], imin*A[i])

            r = max(r, imax)
        return r