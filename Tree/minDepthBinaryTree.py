# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def minDepth(self, root) -> int:
        # bfs 
        if not root: return 0  
        depth = 0 
        queue = deque([(root, 1)]) 
        
        while queue: 
            node, depth = queue.popleft() 
            if not node.left and not node.right: 
                return depth 
            if node.left: 
                queue.append((node.left, depth+1)) 
            if node.right: 
                queue.append((node.right, depth+1)) 
        return depth 

    def minDepth1(self, root) -> int:
        # dfs 
        if not root: return 0 
        depth = float('inf')
        stack = [(root, 1)] 
        
        while stack: 
            node, value = stack.pop() 
            if not node.left and not node.right: 
                depth = min(depth, value)
            if node.right: 
                stack.append((node.right, value+1))
            if node.left: 
                stack.append((node.left, value+1))
        return depth 

    def minDepth2(self, root):
        if not root: return 0
        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d)) # if min(d) == 0: max(d) else: min(d)