class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        # fk genius 
        AB = __import__('collections').Counter(a+b for a in A for b in B) 
        return sum(AB[-c-d] for c in C for d in D)

    def fourSumCount(self, A, B, C, D) -> int:
        d_ = {} 
        c_ = 0 
        for a in A: 
            for b in B: 
                s = a + b 
                d_[s] = d_.get(s, 0) + 1 
        for c in C: 
            for d in D: 
                target = -c-d 
                if target in d_: 
                    c_ += d_[target] 
        return c_