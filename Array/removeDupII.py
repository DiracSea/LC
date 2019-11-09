class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0 
        for n in nums:
            if i < 2 or n > nums[i-2]: 
                nums[i] = n 
                i+=1 
        return i 

    def removeDuplicates1(self, nums) -> int:
        i = 2 
        n = len(nums) 
        while i < n: 
            if nums[i] == nums[i-1] == nums[i-2]: 
                del nums[i] #delete 3rd dup element
                n-=1
            else: 
                i+=1
        return n #n is remaining element number

    