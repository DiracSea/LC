class Solution:
    # two pointers *****
    def minSubArrayLen(self, s: int, nums) -> int: 
        n = len(nums) 
        if n == 0: return 0  
        mi = float("inf") 
        j, res = 0, 0 
        for i in range(0, n): 
            res += nums[i] 
            while res >= s: 
                mi = min(mi, i - j + 1) 
                res -= nums[j] 
                j += 1
        return 0 if mi == float("inf") else mi 

    # o(nlogn)
    def minSubArrayLen1(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left