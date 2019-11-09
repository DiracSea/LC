# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # preorder recursive 
        if not root or root == p or root == q: return root 
        left = self.lowestCommonAncestor(root.left, p, q) 
        right = self.lowestCommonAncestor(root.right, p, q) 
        if left and right: return root # or they track to NoneNode
        return left if left else right

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # preorder iterative 
        stack = [root] 
        parent = {root: None} 
        while p not in parent or q not in parent: 
            node = stack.pop() 
            if node.left: 
                parent[node.left] = node 
                stack.append(node.left) 
            if node.right: 
                parent[node.right] = node 
                stack.append(node.right) 
        
        ancestors = set() 
        while p: 
            ancestors.add(p) # add all p's ancestor
            p = parent[p] # track all p's ancestor
        while q not in ancestors: 
            q = parent[q] # track q's ancestor until overlap 
        return q 