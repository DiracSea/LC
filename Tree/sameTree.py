# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 
class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> bool:
        # iterative
        deq = deque([(p, q),]) 
        while deq: 
            p, q = deq.pop() 
            if not self.check(p, q): 
                return False 
            if p: 
                deq.append((p.right, q.right)) 
                deq.append((p.left, q.left))
        return True 
            
            
    def check(self, p, q): 
        if not p and not q: 
            return True 
        elif not p or not q: 
            return False 
        elif p.val != q.val: 
            return False 
        else: 
            return True

    def isSameTree1(self, p: 'TreeNode', q: 'TreeNode') -> bool:
        # recursive
        if not p and not q: 
            return True 
        
        elif not p or not q: 
            return False 
        
        elif p.val != q.val: 
            return False 
        
        return  self.isSameTree(p.right, q.right) and \
                self.isSameTree(p.left, q.left)