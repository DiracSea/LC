class Solution:
    # rank correct number, then find minimal
    # find minimal first
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        i = 0 
        while i < n: 
            if nums[i] > 0 and nums[i] < n and nums[nums[i] - 1] != nums[i]: # if not the same then swap
                self.swap(nums, nums[i] - 1, i) 
            else: # if it is the same then continue
                i += 1 
        i = 0
        while i < n: 
            if nums[i] != i + 1: # find the mis-locate place 
                return i + 1
            i += 1 
        return n + 1 
                
    def swap(self, nums, a, b): 
        temp = nums[a]
        nums[a] = nums[b] 
        nums[b] = temp 

    # use python feature of list
        
    def firstMissingPositive1(self, nums) -> int:
        i = 1
        while True:
            if i not in nums:
                return i
            i += 1

    # sort list
    def firstMissingPositive2(self, nums) -> int:
        nums = sorted(list({num for num in nums if num > 0}))
        prev = 0
        for num in nums:
            if num - prev > 1:
                return prev + 1
            prev = num
        return prev + 1

    # use index to store freq
    def firstMissingPositive(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
             the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): # delete those useless elements 
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)): # use the index as the hash to record the frequency of each number 
            nums[nums[i]%n] += n 
        for i in range(1,len(nums)): 
            if nums[i]//n == 0: 
                return i 
        return n 