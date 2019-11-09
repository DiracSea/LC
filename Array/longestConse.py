class Solution:
    # sort then check 
    def longestConsecutive(self, nums) -> int: 
        n = len(nums)
        if n < 2: return n 
        nums = sorted(nums) 
        l = 1 
        l_max = 1 
        tmp = nums[0] 
        
        for i in range(1, n): 
            if nums[i] - tmp == 1: 
                l += 1 
                tmp = nums[i] 
                if l_max < l: 
                    l_max = l 
            elif nums[i] == tmp: 
                tmp = nums[i] 
            else: 
                tmp = nums[i] 
                l = 1 
                
        return l_max 

    # set 
    def longestConsecutive1(self, nums) -> int: 
        nums = set(nums) 
        l = 0 
        for n in nums: 
            if n - 1 not in nums: 
                m = n + 1
                while m in nums: 
                    m += 1 
                l = max(l, m - n) 
        return l 