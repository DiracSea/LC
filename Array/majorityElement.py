class Solution: 
    #moore
    def majorityElement(self, nums) -> int:
        major = nums[0] 
        count = 1 
        for i in range(1, len(nums)): 
            if(count == 0): 
                major = nums[i] 
                count = 1 
            elif(major == nums[i]): 
                count+=1 
            else: 
                count-=1 
                
        return major 

    #sorting and select n/2 
    def majorityElement1(self, nums) -> int: 
        return sorted(nums)[len(nums)//2] 

    #hash table

    #divide and conquer

    #bit manipulation 