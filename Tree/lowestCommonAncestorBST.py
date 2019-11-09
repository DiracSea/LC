# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        a, b, c = root.val, p.val, q.val
        if b > c: b, c = c, b 
        if b < a < c: return root 
        elif b == a or c == a: return root 
        elif c < a: return self.lowestCommonAncestor(root.left, p, q) 
        elif b > a: return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        p, q = sorted([p.val, q.val]) 
        while True: 
            if p <= root.val <= q: return root 
            elif root.val > q: root = root.left 
            else: root = root.right 