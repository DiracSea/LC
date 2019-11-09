class Solution:
    def twoSum(self, nums, target: int): 
        d = {}
        for idx, value in enumerate(nums): 
            m = target - value 
            if m in d: 
                return [d[m], idx] 
            else: 
                d[value] = idx 