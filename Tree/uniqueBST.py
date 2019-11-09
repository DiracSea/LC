class Solution:
    def numTrees(self, n: int) -> int:
        # catalan num (2n)!/((n+1)!*n!) 
        f = math.factorial
        return f(2*n)//(f(n)*f(n+1))

    def numTrees1(self, n: int) -> int:
        # dp 
        res = [0]*(n+1) 
        res[0] = 1 
        for i in range(1, n+1): 
            for j in range(i): 
                res[i] += res[j]*res[i-1-j] 
        return res[n]