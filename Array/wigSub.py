class Solution:
    # multiply 
    def wiggleMaxLength(self, nums) -> int:
        n = len(nums) 
        if n == 0: 
            return 0 
        elif n < 2: 
            return 1 
        left = nums[0] 
        output = 0 
        wig = 1 
        dif = 1  
        for i in range(1, n): 
            # first dif != 0 is sure + 1
            if output is 0 and nums[i] - left is not 0: 
                wig += 1 
                dif = nums[i] - left 
                output = max(output, wig)
            # remaining dif 
            elif dif*(nums[i] - left) < 0: 
                wig += 1 
                dif = nums[i] - left 
                output = max(output, wig)
            #else: # no matter what
            left = nums[i] 
        output = max(output, wig)
        return output 

    # short 
    def wiggleMaxLength1(self, nums) -> int:
        nan = float('nan')
        diffs = [a-b for a, b in zip([nan] + nums, nums + [nan]) if a-b]
        return sum(not d*e >= 0 for d, e in zip(diffs, diffs[1:])) # not >= include < and nan 

    # dp 
    def wiggleMaxLength2(self, nums) -> int:
        '''
        1. If nums[i] > nums[i-1], that means it wiggles up. the element before it must be a down position. so             up[i] = down[i-1] + 1; down[i] keeps the same with before.
        2. If nums[i] < nums[i-1], that means it wiggles down. the element before it must be a up position. so             down[i] = up[i-1] + 1; up[i] keeps the same with before.
        3. If nums[i] == nums[i-1], that means it will not change anything becasue it didn't wiggle at all. so             both down[i] and up[i] keep the same.
        ''' 
        n = len(nums) 
        if n is 0: return n 
        up = [0]*n; down = [0]*n 
        up[0] = 1; down[0] = 1
        
        for i in range(1, n): 
            if nums[i] > nums[i - 1]: 
                up[i] = down[i - 1] + 1 
                down[i] = down[i - 1] 
            elif nums[i] < nums[i - 1]: 
                up[i] = up[i - 1] 
                down[i] = up[i - 1] + 1 
            else: 
                down[i] = down[i - 1] 
                up[i] = up[i - 1] 
        return max(down[n - 1], up[n - 1])