class Solution: 
    #  Kadane's algorithm
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)): 
            if nums[i-1] > 0: 
                nums[i] += nums[i-1]
            
        return max(nums) 

    # divide and conquer 
    def maxSubArray1(self, A) -> int:
        maxSoFar = A[0] 
        maxEndHere = A[0] 
        for i in range(1, len(A)): 
            maxEndHere = max(maxEndHere+A[i], A[i]) 
            maxSoFar = max(maxSoFar, maxEndHere)
            
        return maxSoFar  

    # dp 
    def maxSubArray2(self, A) -> int: 
        n = len(A) 
        dp = [0]*n 
        dp[0] = A[0] 
        m = dp[0] 

        for i in range(1, n): 
            dp[i] = A[i] + (dp[i-1] if dp[i-1] > 0 else 0) 
            m = max(m, dp[i])
        return m