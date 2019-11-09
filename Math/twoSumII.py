class Solution:
    def twoSum(self, numbers, target: int):
        d = {} 
        for idx, value in enumerate(numbers): 
            m = target - value 
            if m in d: 
                return [d[m]+1, idx+1] 
            else: 
                d[value] = idx 