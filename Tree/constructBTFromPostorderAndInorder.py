# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if not inorder or not postorder: return
        # idx = inorder.index(postorder.pop()) 
        # root = TreeNode(inorder[idx]) 
        root = TreeNode(postorder.pop()) 
        idx = inorder.index(root.val) 
        
        root.right = self.buildTree(inorder[idx+1:], postorder) 
        root.left = self.buildTree(inorder[:idx], postorder) 

        return root 

    def buildTree1(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        # map 
        d = {} 
        for idx, val in enumerate(inorder): d[val] = idx 
        
        def rec(low, high): 
            if low > high: return 
            root = TreeNode(postorder.pop()) 
            mid = d[root.val] 
            root.right = rec(mid+1, high) 
            root.left = rec(low, mid-1) 
            return root 
        return rec(0, len(inorder)-1)