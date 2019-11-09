# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root) -> int:
        global m
        m = float('-inf')
        self.maxToRoot(root) 
        return m 
    
    def maxToRoot(self, node): 
        if not node: return 0 
        global m
        
        l = max(self.maxToRoot(node.left), 0) 
        r = max(self.maxToRoot(node.right), 0) 
        
        m = max(m, node.val + l + r) 
        
        return node.val + max(l, r) 