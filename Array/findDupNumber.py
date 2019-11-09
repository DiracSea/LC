class Solution:
    def findDuplicate(self, nums):
        left, right = 1, len(nums) - 1
        while left < right : 
            mid = left + (right - left) // 2
            count = 0
            for k in nums:
                if mid < k <= right:
                    count += 1
            if count > right - mid:
                left = mid + 1
            else:
                right = mid
        return right


    def findDuplicate1(self, nums) -> int:
        foundNums = {}
        
        for i in nums:
            if i not in foundNums:
                foundNums[i] = 1
            else:
                return i
    def findDuplicate2(self, nums) -> int:
        map = {}
        for i,n in enumerate(nums):
            if not n in map: map[n] = 1
            else: return n