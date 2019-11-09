class Solution:
    def threeSum(self, num):
        output = [] 
        n = len(num) 
        num = sorted(num) # use sort to eliminate dup combo 
        
        for i in range(n - 2): 
            if num[i] > 0: # remain nums are postive
                break 
            if i > 0 and num[i] == num[i-1]: # jump over dup
                continue 
            
            l, r = i+1, n-1 # window
            # use smallest two add biggest one 
            while l < r: 
                total = num[i] + num[l] + num[r] 
                
                if total < 0: # move right 
                    l += 1 
                elif total > 0: # move left 
                    r -= 1 
                else: # add 
                    output.append([num[i], num[l], num[r]]) 
                    while l < r and num[l] == num[l+1]: 
                        l += 1 # jump dup 
                    while l < r and num[r] == num[r-1]: 
                        r -= 1 # jump dup
                    l += 1 
                    r -= 1
        return output 

    def threeSum1(self, nums):
        return self.threeTarget(nums, 0)
    
    def threeTarget(self, nums, target): 
        ans = [] 
        counts = {} 
        for i in nums: 
            counts[i] = counts.get(i, 0) + 1
        nums = sorted(counts) 
        for i, num in enumerate(nums): 
            if counts[num] >= 2: # over 2 dup num
                if num == 0: # 0
                    if counts[num] >= 3: 
                        ans.append([0,0,0])
                else: 
                    if target - 2*num in nums: 
                        ans.append([num,num,-2*num])
            
            if num < 0: 
                twosum = target - num # compute twosum
                '''
                bisect.bisect_left(a, x, lo=0, hi=None)
                a insert x
                bisect.bisect_right(a, x, lo=0, hi=None)
                '''
                l = bisect.bisect_left(nums, (twosum-nums[-1]), i+1) 
                for i in nums[l:bisect.bisect_right(nums, (twosum//2), l)]: 
                    j = twosum-i 
                    if j in counts and j != i: 
                        ans.append([num, i, j])
        return ans 