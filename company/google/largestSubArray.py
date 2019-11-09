class Solution: 

    # O(n)
    def largest_sub(self, A, k):
        large_idx = 0 
        n = len(A)

        for i in range(1, n-k+1): 
            if A[i] > A[large_idx]: 
                large_idx = i 
        
        return A[large_idx:large_idx+k]

    # nondistinct
    def largest_sub_non_distinct(self, A, k): 
        large_A = A[:k] 
        n = len(A)

        for i in range(1, n-k+1): 
            large_A = self.compare(large_A, A[i:i+k], k)
        return large_A

    def compare(self, A1, A2, k): 
        for i in range(k): 
            if A1[i] > A2[i]: 
                return A1 
            elif A2[i] > A1[i]: 
                return A2
            else: 
                continue
        return A1

        