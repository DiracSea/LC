class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, dist in enumerate(nums): 
            if reach < i: 
                return False 
            reach = max(reach, i + dist) 
            #if reach >= len(nums) - 1: return True   : rebundant
        return True

    def canJump1(self, nums: List[int]) -> bool:
        reach = 0
        for i, item in enumerate(nums): 
            if i <= reach: 
                if i + item > reach: 
                    reach = i + item 
            else: 
                break 
        return reach >= len(nums) - 1


    def canJump2(self, nums: List[int]) -> bool: 
        goal = len(nums) - 1
        for i range(len(nums))[::-1]: 
            if i + nums[i] >= goal: 
                goal = i 
        return not goal 