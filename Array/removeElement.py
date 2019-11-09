
class Solution:
    #def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while True:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)

    def removeElement1(self, nums, val):
        i = 0
        for j in nums:
            if j != val:
                nums[i] = j
                i+=1
        return i