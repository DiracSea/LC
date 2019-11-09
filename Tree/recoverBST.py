# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: 
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # left st root, right bt root
        # inorder shoud be ascend
        # find the mixmatch two nodes 
        # or build list 
        self.first, self.second, self.prev = None, None, TreeNode(float('-inf'))
        self.inorder(root) 
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def inorder(self, root): 
        
        if not root: return 
        self.inorder(root.left) 
        
        if not self.first and self.prev.val >= root.val: 
            self.first = self.prev 
            
        if self.first and self.prev.val >= root.val: 
            self.second = root 
            
        self.prev = root 
        
        self.inorder(root.right)

             