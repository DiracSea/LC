class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        # Bucket Sort 
        '''
        1,4,5,9; 2; 3
        (1) the two in the same bucket 4,5
        (2) the two in neighbor buckets 1,4
        '''
        if k < 0 or t < 0: return False  
        d = {} 
        w = t + 1
        for i in range(len(nums)): 
            m = nums[i]//w 
            if m in d:
                return True 
            elif m - 1 in d and abs(nums[i] - d[m - 1]) < w: 
                return True 
            elif m + 1 in d and abs(nums[i] - d[m + 1]) < w: 
                return True 
            d[m] = nums[i] 
            if i >= k: del d[nums[i - k]//w] # remove element out of window
        return False
            
        