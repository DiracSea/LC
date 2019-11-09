# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # brute force
    def countNodes(self, root: TreeNode) -> int:
        # preorder 
        self.num = 0 
        if not root: return self.num 
        self.dfs(root) 
        return self.num 
    
    def dfs(self, root): 
        if not root: return 
        self.num += 1 
        self.dfs(root.left) 
        self.dfs(root.right)

    def countNodes1(self, root: TreeNode) -> int:
### perfect
        '''
        If left sub tree height equals right sub tree height then,
        a. left sub tree is perfect binary tree
        b. right sub tree is complete binary tree
        If left sub tree height greater than right sub tree height then,
        a. left sub tree is complete binary tree
        b. right sub tree is perfect binary tree
        '''
        # divide and conquer
        # Ologn*logn 
        # compare leftsub and rightsub 
        if not root: return 0 
        leftD = self.getD(root.left) 
        rightD = self.getD(root.right) 
        
        if leftD == rightD: 
            return (1 << leftD) + self.countNodes1(root.right) 
        else: 
            return (1 << rightD) + self.countNodes1(root.left) 
        
    def getD(self, root): 
        if not root: return 0 
        return 1 + self.getD(root.left)