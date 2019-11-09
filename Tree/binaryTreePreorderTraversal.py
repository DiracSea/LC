# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        # recursive 
        values = []
        if root: 
            self.preorder(root, values)
        return values
        
    def preorder(self, node, values): 
        if node: 
            values.append(node.val) 
            self.preorder(node.left, values) 
            self.preorder(node.right, values) 

    def preorderTraversal1(self, root):
        '''
          1
         / 
        2 - 3
        '''
        # iteratively 
        res = [] 
        if root: 
            stack = [root] 
            
            while stack: 
                node = stack.pop() 
                if node: 
                    res.append(node.val) 
                    # stack right in left out| first in last out
                    if node.right: 
                        stack.append(node.right) 
                    if node.left: 
                        stack.append(node.left) 
                           
        return res 