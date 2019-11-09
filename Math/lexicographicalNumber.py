class Solution:
    def lexicalOrder(self, n: int): 
        # dfs 
        # use tree 
        '''
          1
         / \
        10-19
        '''
        res = [] 
        for i in range(1, 10): 
            self.dfs(i, n, res) 
        return res 
    
    def dfs(self, cur: int, n: int, res): 
        if cur > n: 
            return 
        else: 
            res.append(cur) 
            for i in range(10): 
                if 10*cur + i > n: 
                    return 
                self.dfs(10*cur + i, n, res)

    def lexicalOrder1(self, n: int): 
        # O1 space 
        ans = [1] 
        while len(ans) < n: 
            new = ans[-1]*10 # increase digit until bt n 
            '''
            n = 1001
            1 10 100 1000
            (10000)1001 (1002)101 (1010)102 ... (1020) 102
            
            '''
            while new > n: 
                new //= 10 
                new += 1 
                while not new%10: ## deal with case like 199+1=200
                    new //= 10 
            ans.append(new)
        return ans 

    def lexicalOrder2(self, n: int): 
        return sorted(range(1, n+1), key=str)