class Solution:
    # brute force  
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums) 
        
        if n == 0: 
            return [] 
        elif n == k: 
            return [max(nums)] 
        
        output = [] 
        for i in range(0, n - k + 1): 
            output.append(max(nums[i: i + k])) 
        return output 
    
    def maxSlidingWindow1(self, nums, k: int):
        n = len(nums) 
        
        if n == 0: 
            return [] 
        elif n == k: 
            return [max(nums)] 
        
        for i in range(0, n - k + 1): 
            nums[i] = max(nums[i: i + k])
        return nums[0: n - k + 1] 

    # deque
    def maxSlidingWindow2(self, nums, k: int):
        import collections
        d = collections.deque()
        res = []
        for i, n in enumerate(nums):
            while d and n > d[-1]:
                d.pop()
            d.append(n)
            if i > k-1 and d[0] == nums[i-k]:
                d.popleft()
            if i >= k-1:
                res.append(d[0])
        return res
    
