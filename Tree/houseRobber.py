# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    # TLE
    def rob0(self, root) -> int:
        # 1 + 3, 2
        if not root: return 0 
        return max(self.include(root), self.exclude(root)) 
    
    def include(self, node): 
        if not node: return 0 
        return self.exclude(node.left) + self.exclude(node.right) + node.val 
    
    def exclude(self, node): 
        if not node: return 0 
        return self.rob0(node.left) + self.rob0(node.right) 


    # optimization
    # 1
    def rob1(self, root) -> int:
        if not root: return 0 
        
        val = 0 
        
        if root.left: 
            val += self.rob1(root.left.left) + self.rob1(root.left.right) 
        if root.right: 
            val += self.rob1(root.right.left) + self.rob1(root.right.right) 
            
        return max(val + root.val, self.rob1(root.left) + self.rob1(root.right))

    # 2
    def rob2(self, root) -> int:
        return self.robSub(root, dict())
    
    def robSub(self, root, d): 
        if not root: return 0 
        if d.get(root, 0): return d[root] 
        
        val = 0 
        if root.left: 
            val += self.robSub(root.left.left, d) + self.robSub(root.left.right, d) 
            
        if root.right: 
            val += self.robSub(root.right.left, d) + self.robSub(root.right.right, d) 
            
        val = max(val + root.val, self.robSub(root.left, d) + self.robSub(root.right, d)) 
        d[root] = val 
        
        return val

    # 3 
    def rob3(self, root) -> int:
        res = self.robSub1(root)
        return max(res[0], res[1])
    
    def robSub1(self, root): 
        if not root: return [0]*2 
        
        l = self.robSub1(root.left) 
        r = self.robSub1(root.right) 
        res = [0]*2 
        
        res[0] = max(l[0], l[1]) + max(r[0], r[1]) 
        res[1] = root.val + l[0] + r[0] 
        
        return res 

    # dfs and greedy

    def rob4(self, root) -> int:
        return self.dfs(root)[1] 
        
    def dfs(self, root): 
        if not root: return [0, 0] 
        l = self.dfs(root.left) 
        r = self.dfs(root.right) 
        not_use = l[1] + r[1] 
        max_val = max(not_use, l[0] + r[0] + root.val) 
        
        return [not_use, max_val]