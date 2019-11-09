# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        # triangle 
        # preorder -> root 
        # inorder -> subtree
        if inorder: 
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx]) 
            root.left = self.buildTree(preorder, inorder[:idx]) 
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root 

    def buildTree1(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        # map
        
        def helper(left_in = 0, right_in = len(inorder)): 
            nonlocal idx_pre 
            
            if left_in == right_in: return 
            
            root_val = preorder[idx_pre] 
            root = TreeNode(root_val) 
            
            idx = idx_map[root_val] 
            
            idx_pre += 1 
            root.left = helper(left_in, idx) 
            root.right = helper(idx + 1, right_in) 
            return root 
        idx_pre = 0 
        idx_map = {val: idx for idx,val in enumerate(inorder)} 
        return helper()

        