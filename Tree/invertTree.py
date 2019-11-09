# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode': 
        # bfs
        if not root: return root 
        stack = [root]
        while stack: 
            length = len(stack)
            for _ in range(length): 
                node = stack.pop() 
                if node.left: 
                    stack.append(node.left) 
                if node.right: 
                    stack.append(node.right)
                self.swap(node) 
        
        return root 
    
    def swap(self, node): 
        p = node.left 
        q = node.right 
        if not p and not q: 
            return 
        else: 
            node.left = q 
            node.right = p

    # recursive DFS
    def invertTree1(self, root: 'TreeNode') -> 'TreeNode': 
        if not root: return
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left) 
        self.invertTree(root.right)
        
        return root 


    # preorder, slower
    def invertTree2(self, root: 'TreeNode') -> 'TreeNode': 
        if not root: return root 
        stack = [root]
        while stack: 
            node = stack.pop() 
            self.swap(node) 
            if node.left: 
                stack.append(node.left) 
            if node.right: 
                stack.append(node.right)
        
        return root 

    # more readable
    def invertTree3(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root