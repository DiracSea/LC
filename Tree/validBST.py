# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root) -> bool:
        # bound 
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, node, lower, upper): 
        if not node: return True 
        if node.val >= upper or node.val <= lower: return False 
        
        l = self.helper(node.left, lower, node.val) 
        r = self.helper(node.right, node.val, upper) 
        return l and r 

    def isValidBST1(self, root) -> bool:
        # inorder
        self.arr = [] 
        self.inorder(root) 
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))
    
    def inorder(self, root): 
        if not root: return 
        self.inorder(root.left) 
        self.arr.append(root.val) 
        self.inorder(root.right) 
         
    # space optimization 
    def isValidBST2(self, root) -> bool:
        # inorder
        self.last = float('-inf') 
        self.flag = True
        self.inorder(root) 
        return self.flag
    
    def inorder(self, root): 
        if not root: return 
        self.inorder(root.left) 
        if self.last >= root.val: self.flag = False
        self.last = root.val 
        self.inorder(root.right) 

    def isValidBST3(self, root) -> bool:
        # inorder iterative 
        stack = [] 
        pre = None # last node 
        while stack or root: # inorder  
            while root: 
                stack.append(root) 
                root = root.left 
            root = stack.pop() 
            if pre and pre.val >= root.val: 
                return False 
            pre = root 
            root = root.right 
        return True
         