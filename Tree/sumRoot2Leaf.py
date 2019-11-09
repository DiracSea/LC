# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    # dfs 
    def sumNumbers(self, root: 'TreeNode') -> int:
        res = 0 
        if not root: return res 
        stack = [(root, root.val)]
        while stack: 
            node, cur = stack.pop() 

            if not node.left and not node.right: 
                res += cur 
            if node.right: 
                stack.append((node.right, cur*10 + node.right.val)) 
            if node.left: 
                stack.append((node.left, cur*10 + node.left.val))
        return res 
    
    # bfs 
    def sumNumbers1(self, root: 'TreeNode') -> int:
        res = 0 
        if not root: return res 
        
        queue = deque([(root, root.val)]) 
        while queue: 
            node, value = queue.popleft() 
            
            if not node.left and not node.right: 
                res += value 
            if node.left: 
                queue.append((node.left, node.left.val + 10*value)) 
            if node.right: 
                queue.append((node.right, node.right.val + 10*value)) 
                
        return res 