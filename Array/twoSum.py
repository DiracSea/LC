class Solution:
    def twoSum(self, nums, target: int): 
        d = {}
        for i, j in enumerate(nums): 
            m = target - j 
            if m in d:
                return [d[m], i]
            else:
                d[j] = i