# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root) -> int:
        if not root: return 0
        d = map(self.maxDepth, (root.left, root.right)) 
        return 1 + max(d)

    def maxDepth1(self, root) -> int:
        if not root: return 0
        stack =  [(root, 1)] 
        depth = 0 
        
        while stack: 
            node, value = stack.pop() 
            if not node.left and not node.right: 
                depth = max(depth, value) 
                
            if node.right: 
                stack.append((node.right, value+1)) 
                
            if node.left: 
                stack.append((node.left, value+1)) 
        return depth 