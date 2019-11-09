class Solution:
    def fourSum(self, nums, target: int):
        s = set() 
        nums = sorted(nums) 
        n = len(nums)
        for i in range(1, n - 2): 
            if i > 1 and nums[i] == nums[i-2]:
                continue
            for j in range(i):   
                if j > 0 and nums[j] == nums[j-1]: 
                    continue
                    
                l, r = i+1, n-1 
                
                while l < r: 
                    total = nums[j] + nums[i] + nums[l] + nums[r] 
                    # print(total)
                    if total == target: 
                        s.add((nums[j], nums[i], nums[l], nums[r])) 
                        while l < r and nums[l] == nums[l+1]: 
                            l += 1 
                        while l < r and nums[r] == nums[r-1]: 
                            r -= 1 
                        l += 1 
                        r -= 1
                    elif total > target: 
                        r -= 1 
                    else: 
                        l += 1 
        return list(map(list, s))

    def fourSum(self, nums, target: int):
        #  implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum
        nums.sort() 
        res = [] 
        self.findN(nums, target, 4, [], res) 
        return res 
    
    def findN(self, nums, target, N, ans, res): 
        if len(nums) < N or N < 2: return 
        # solve 2sum 
        if N == 2: 
            l, r = 0, len(nums) - 1
            while l < r: 
                if nums[l] + nums[r] == target: 
                    res.append(ans+[nums[l],nums[r]]) 
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1 
                    while l < r and nums[r] == nums[r+1]: 
                        r -= 1
                elif nums[l] + nums[r] < target: 
                    l += 1 
                else: 
                    r -= 1 
        else: 
            for i in range(len(nums)-N+1): 
                if target < nums[i]*N or target > nums[-1]*N: 
                    break 
                if i == 0 or i > 0 and nums[i-1] != nums[i]: # recusively reduce N 
                    self.findN(nums[i+1:], target-nums[i], N-1, ans+[nums[i]], res) 
        return 