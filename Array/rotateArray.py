class Solution:
    # brute force
    # time exceed
    def rotate(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        for i in range(k): 
            pre = nums[n - 1] 
            for j in range(n): 
                tmp = nums[j] 
                nums[j] = pre 
                pre = tmp 

    # extra array
    # low efficiency
    def rotate1(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        tmp = [0 for i in range(n)]
        for i in range(n): 
            tmp[(i + k) % n] = nums[i] 
        nums[:] = tmp[:]

    # clean and very quick
    def rotate2(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]

    # clean but very slow
    def rotate3(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1 
    
    # reverse slow
    def rotate4(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        k %= n
        if n > 1:
            self.reverse(nums, 0, n - 1) 
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)
    
    def reverse(self, nums, head, tail): 
        while head < tail: 
            tmp = nums[head] 
            nums[head] = nums[tail]
            nums[tail] = tmp 
            head += 1
            tail -= 1