# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isSymmetric(self, root: 'TreeNode') -> bool:
        # /- == -\
        # iterative 
        deq = deque([(root, root), ])
        while deq: 
            p, q = deq.pop() 
            if not self.isSame(p, q): 
                return False 
            if p: 
                deq.append((p.right, q.left)) 
                deq.append((p.left, q.right)) 
        return True
        
    def isSame(self, p, q): 
        if not p and not q: 
            return True 
        elif not p or not q: 
            return False 
        elif p.val != q.val: 
            return False 
        else: 
            return True 

    def isSymmetric1(self, root: 'TreeNode') -> bool:
        # /- == -\
        # recursive 
        return self.check(root, root)
    
    def check(self, p, q):
        if not p and not q: 
            return True 
        elif not p or not q: 
            return False 

        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)