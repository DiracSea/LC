class Solution:
    def productExceptSelf(self, nums): 
        # two loop, 
        # 1st loop go ahead, stop till the cur 
        # 2nd loop go back, stop in the cur 
        output = [] 
        p = 1 
        n = len(nums) 
        for i in nums: 
            output.append(p) 
            p *= i 
        '''
        or
        n = len(nums)
        output = [1]*n
        for i in range(1, n): 
            output[i] *= output[i - 1]
        '''
        
        p = 1
        for i in range(n - 1, -1, -1): 
            output[i] *= p 
            p *= nums[i]
        
        return output 

    