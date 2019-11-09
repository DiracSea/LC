def Solution: 
    def maxNumber(self, nums1, nums2, k):
        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a+b] 
            '''
            The max(a, b).pop(0) takes the first element from the (lexicographically) larger of the two lists.
            The for _ in a+b is just a hack effectively meaning "do it k times".
            So the result is the list that I get by k times taking the first element from the (lexicographically) larger list.
            '''

        return max(merge(prep(nums1, i), prep(nums2, k-i))
                for i in range(k+1)
                if i <= len(nums1) and k-i <= len(nums2))