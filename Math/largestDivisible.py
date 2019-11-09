class Solution:
    def largestDivisibleSubset(self, nums):
        # dp 
        from copy import copy 
        nums.sort() 
        n = len(nums) 
        if not n: return []
        dp = [0]*n 
        dp[0] = [nums[0]] 
        
        for i in range(1, n): 
            cur = nums[i] 
            maxSet = [] 
            for j in range(i): # use every element % left elements 
                if cur%nums[j] == 0: 
                    localSet = copy(dp[j]) 
                    if len(localSet) > len(maxSet): 
                        maxSet = localSet 
            
            maxSet.append(nums[i]) 
            dp[i] = maxSet 
            
        res = [] 
        for localSet in dp: 
            if len(localSet) > len(res): 
                res = localSet 
        return res 
                
    def largestDivisibleSubset1(self, nums):
        # 
        nums.sort() 
        res = {} 
        if not nums: 
            return [] 
        for i in nums: 
            val = [] 
            for key in res: # key is front, i is rear 
                if not i%key: 
                    if len(res[key]) > len(val): # if key is the factors of i, all factors of key is i's
                        val = res[key] 
            res[i] = val + [i] # find all factors of each i 
        val = [] 
        
        for key in res: 
            if len(res[key]) > len(val): 
                val = res[key] 
        
        return val 

    def largestDivisibleSubset2(self, nums):

        S = {-1: set()} 
        for x in sorted(nums): 
            S[x] = max((S[d] for d in S if x%d == 0), key = len) | {x} 
        return list(max(S.values(), key = len))