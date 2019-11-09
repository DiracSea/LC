class Solution:
    # sort and compare
    def containsDuplicate(self, nums) -> bool:
        n = len(nums) 
        if n < 2: 
            return False 
        nums = sorted(nums) 
        for i in range(1, n): 
            if(nums[i-1] == nums[i]): 
                return True 
        return False 

    # set 
    def containsDuplicate1(self, nums) -> bool:
        return len(nums) > len(set(nums))

    # set
    def containsDuplicate2(self, nums) -> bool:
        s = set() 
        for i in nums: 
            if i in s: 
                return True
            else: 
                s.add(i) 
        return False