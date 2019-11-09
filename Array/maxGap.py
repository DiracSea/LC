    def maximumGap(self, nums) -> int:
        nums = sorted(nums)
        n = len(nums) 
        if n < 2: return 0 
        gap = 0 
        left = float("inf") 
        for i in nums:  
            gap = max(gap, i - left) 
            left = i 
        return gap 