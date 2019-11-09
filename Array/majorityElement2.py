class Solution: 
    # moore voting 
    def majorityElement(self, nums) -> List[int]:
    if not nums: 
        return [] 
    major1, major2, count1, count2 = 1, 0, 0, 0
    
    for n in nums: 
        if(n == major1): 
            count1+=1 
        elif(n == major2): 
            count2+=1 
        elif(count1 == 0): 
            major1, count1 = n, 1 
        elif(count2 == 0): 
            major2, count2 = n, 1 
        else: 
            count1-=1 
            count2-=1 
    return [n for n in (major1, major2) if nums.count(n) > len(nums)//3]