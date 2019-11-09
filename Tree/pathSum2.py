# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 
class Solution:
    def pathSum(self, root: 'TreeNode', s: int) -> 'List[List[int]]':
        # dfs + stack 
        if not root: # root is None, s is 0 return False 
            return [] 

        res, stack = [], [(root, [root.val])] 

        while stack: 
            node, value = stack.pop() 
            if not node.left and not node.right: 
                if sum(value) == s: 
                    res.append(value)
            if node.right: 
                stack.append((node.right, value + [node.right.val])) 
            if node.left: 
                stack.append((node.left, value + [node.left.val])) 
        return res 

    def pathSum1(self, root: 'TreeNode', s: int) -> 'List[List[int]]':
        # bfs + queue 
        if not root: # root is None, s is 0 return False 
            return [] 

        res, queue = [], deque([(root, [root.val])])

        while queue: 
            node, value = queue.popleft() 
            if not node.left and not node.right: 
                if sum(value) == s: 
                    res.append(value)
            if node.left: 
                queue.append((node.left, value + [node.left.val]))
            if node.right: 
                queue.append((node.right, value + [node.right.val]))  
        return res 