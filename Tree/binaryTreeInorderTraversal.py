# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        res = [] 
        if root:  
            self.inorder(root, res)
        return res
        
    def inorder(self, node, res): 
        if node: 
            self.inorder(node.left, res) 
            res.append(node.val) 
            self.inorder(node.right, res)

    def inorderTraversal1(self, root):
        '''
          2
         / \
        1   3
        '''
        res = [] 
        stack = [] 
        node = root 
        while stack or node: 
            while node: # all left in stack
                stack.append(node) 
                node = node.left 
            
            # from left track
            node = stack.pop() 
            res.append(node.val) 
            node = node.right # enter right tree
                
        return res 