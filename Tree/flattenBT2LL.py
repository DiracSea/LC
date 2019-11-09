# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # preorder 
        if not root: return None
        if not root.left and not root.right: return root 
        self.nodes = [] 
        self.dfs(root)
        node = root 
        for n in self.nodes: 
            node.right = n 
            node.left = None
            node = n
        
    def dfs(self, node): 
        if not node: return 
        self.nodes.append(node) 
        if node.left: 
            self.dfs(node.left) 
        if node.right: 
            self.dfs(node.right)

class Solution1:
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # reverse preorder
        '''
          3
         /
        2 - 1
        '''
        
        self.prev = None 
        self.dfs(root)
        
    def dfs(self, root): 
        if not root: return 
        self.dfs(root.right) 
        self.dfs(root.left) 
        
        root.right = self.prev 
        root.left = None 
        self.prev = root 