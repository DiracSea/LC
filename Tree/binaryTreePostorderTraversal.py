# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = [] 
        if root: 
            self.postorder(root, res) 
        return res 
        
    def postorder(self, node, res): 
        if node: 
            self.postorder(node.left, res) 
            self.postorder(node.right, res) 
            res.append(node.val)

    def postorderTraversal1(self, root):
        '''
          3
           \
        1 - 2
        '''
        if not root: return [] 
        res = [] 
        stack = [(root, False)] 
        while stack: 
            node, visited = stack.pop() 
            if visited: 
                res.append(node.val) 
            else: 
                stack.append((node, True)) # last 
                if node.right: 
                    stack.append((node.right, False)) # second 
                if node.left: 
                    stack.append((node.left, False)) # first 
        return res

    def postorderTraversal2(self, root):
        '''
          1            3
           \    ->      \
        3 - 2        1 - 2
        '''
        stack = [root] 
        res = [] 
        while stack: 
            node = stack.pop() 
            
            if node: 
                stack.append(node.left) # third
                stack.append(node.right) # second
                
                res.append(node.val) # first 
        
        return reversed(res) 

    def postorderTraversal3(self, root):
        '''
           3
            \
         1 - 2
        '''
        # reverse inorder
        stack = [] 
        res = [] 
        node = root 
        while node or stack: 
            while node: 
                stack.append(node) 
                res.insert(0, node.val) 
                node = node.right 
                
            popped = stack.pop() 
            node = popped.left 
            
        return res 

    def postorderTraversal4(self, root):
        # no reverse or insert 
        res, stack = [], [] 
        if not root: return [] 
        node = root 
        last = None 
        while node or stack: 
            while node: 
                stack.append(node) 
                node = node.left 
            peek = stack[-1] 
            if peek.right and last != peek.right: 
                node = peek.right 
            else: 
                peek = stack.pop() 
                res.append(peek.val) 
                last = peek 
        return res 