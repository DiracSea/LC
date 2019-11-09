class Solution:
    # space-saving
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return 0

        last = nums[-1]
        for i in reversed(range(len(nums[:-1]))):
            if nums[i] == last:
                nums.pop(i)
            else:
                last = nums[i]

        return len(nums)
    
    # time-saving
    def removeDuplicates1(self, nums: 'List[int]') -> 'int':
        i = 0
        if len(nums) == 0: 
            return 0 
        for j in nums: 
            if nums[i] != j: 
                i+=1 
                nums[i] = j 
        return i+1