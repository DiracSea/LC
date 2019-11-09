class Solution:
    def sortColors(self, A) -> None:
        # counting sort 
        one, two, zero = 0, 0, 0 
        for i in A: 
            if i == 1: 
                one += 1 
            elif i == 2: 
                two += 1 
            else: 
                zero += 1 
        
        for i in range(0, len(A)): 
            if i < zero: 
                A[i] = 0 
            elif i >= zero and i < one + zero: 
                A[i] = 1 
            else: 
                A[i] = 2 

    def sortColors1(self, nums) -> None:
        # one pass 
        i = j = 0
        for k in range(len(nums)):
            # cur to largest
            v = nums[k]
            nums[k] = 2
            # if original is less than 2 then it should be 1
            if v < 2:
                nums[j] = 1
                j += 1
            # if original is less than 1 then it should be 0. The above if statement ensures that 1 - index 
            # will always be greater than 0 - index
            if v == 0:
                nums[i] = 0
                i += 1
                
    def sortColors2(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:# 1 < 2
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red] # swap 0 and 1
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white] # swap 1 and 2
                blue -= 1