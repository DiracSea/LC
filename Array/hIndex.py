class Solution: 
    # sort then find
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations) 
        count = 0 
        citations = sorted(citations)
        for i in range(0, n): 
            idx = n - i - 1 
            if citations[idx] <= i: # i is idx not number 
                break 
            count+=1
        return count

    # 1 line
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse = True)))