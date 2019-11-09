class Solution:
    def partition(self, s: str):
        # backtracking 
        def isP(s): 
            return s == s[::-1] 
        
        def dfs(s, path, res): 
            if not s: 
                res.append(path[:]) # add path to res 
                return # backtracking
            for i in range(1, len(s) + 1): 
                if isP(s[:i]): 
                    # path.append(s[:i]) # add palin to path 
                    dfs(s[i:], path+[s[:i]], res) # add remaining palin to path 
                    # path.pop() 
        
        res = [] 
        dfs(s, [], res) 
        return res 

    def partition1(self, s: str):
        # backtracking 
        return [[s[:i]] + rest
                for i in range(1, len(s)+1)
                if s[:i] == s[i-1::-1]
                for rest in self.partition(s[i:])] or [[]]