# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # inorder build list recursion    
    def kthSmallest(self, root: 'TreeNode', k: int) -> int: 
        def inorder(n): 
            return inorder(n.left) + [n.val] + inorder(n.right) if n else [] 
        return inorder(root)[k-1]

    # inorder recursion    
    def kthSmallest1(self, root: 'TreeNode', k: int) -> int: 
        self.k = k 
        self.res = None 
        self.helper(root) 
        return self.res 
    
    def helper(self, node): 
        if not node: return 
        self.helper(node.left) 
        self.k -= 1 
        if self.k == 0: 
            self.res = node.val 
            return 
        self.helper(node.right)

    # inorder iterative    
    def kthSmallest2(self, root: 'TreeNode', k: int) -> int: 
        stack = [] 
        while root or stack: 
            while root: 
                stack.append(root) 
                root = root.left 
            root = stack.pop() 
            k -= 1 
            if not k: return root.val 
            root = root.right 