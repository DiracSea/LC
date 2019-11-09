class Solution:
    def hIndex(self, citations: List[int]) -> int: 
        count = 0 
        n = len(citations)
        for i in range(n): 
            idx = n - i - 1 
            if (citations[idx] > i): 
                count += 1
        return count  
            