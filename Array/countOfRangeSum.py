class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:
        # merge sort 
        first = [0] 
        for num in nums: 
            first.append(first[-1] + num) 
        # [-2, 5, -1]: [0, -2, 3, 2] 
        def countSort(lo, hi): 
            mid = (lo + hi)//2 
            if mid == lo: 
                return 0 
            count = countSort(lo, mid) + countSort(mid, hi) 
            i = j = mid 
            for left in first[lo:mid]: 
                while i < hi and first[i] - left < lower: i += 1 
                while j < hi and first[j] - left <= upper: j += 1 
                count += j - i # (-inf, upper) - (-inf, lower) 
            first[lo:hi] = sorted(first[lo:hi]) 
            return count 
        return countSort(0, len(first))
                
            
            
            