class Solution:
    #############################
    def numDistinct(self, s: str, t: str) -> int:
        # s short t long 
        # mem (t+1) items, (s+1) lines
        m = len(s); n = len(t)
        # mem = [[0]*(n+1)]*(m+1) totally wrong method 
        mem = [[0]*(n+1) for _ in range(m+1)]
        
        # fill 1st row with 1 
        for i in range(m): 
            mem[i][0] = 1 
        
        for i in range(1, m+1): 
            for j in range(1, n+1): 
                if s[i - 1] == t[j - 1]: 
                    mem[i][j] = mem[i-1][j-1] + mem[i-1][j] 
                else: 
                    mem[i][j] = mem[i-1][j] 
        
        return mem[-1][-1]