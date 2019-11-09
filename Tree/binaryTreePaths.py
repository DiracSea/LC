# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # preorder
    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        res = [] 
        if root: 
            self.preorder(res, root, "") 
        return res 
    
    def preorder(self, res, node, path): 
        if not node: return # if none node, end  
        
        # path.append(str(node.val)) 
        if not path: 
            path += str(node.val)
        else: 
            path += '->' + str(node.val) 
        
        if node.left or node.right: # 
            self.preorder(res, node.left, path) 
            self.preorder(res, node.right, path) 
            
        else: 
            res.append(path) # only the leaf will be added 

    def binaryTreePaths1(self, root: 'TreeNode') -> 'List[str]':
        # preorder
        # dfs + stack 
        if not root: 
            return [] 
        
        res, stack = [], [(root, "")] # store node and path at the same time 
        while stack: 
            node, path = stack.pop() 
            if not node.left and not node.right: 
                res.append(path + str(node.val)) # leaf add past path and its value 
                
            if node.right: 
                stack.append((node.right, path + str(node.val) + '->')) 
                # right first in 
            if node.left: 
                stack.append((node.left, path + str(node.val) + '->')) 
                # left last in 
        return res 

    def binaryTreePaths2(self, root: 'TreeNode') -> 'List[str]':
        # bfs + queue

        if not root: 
            return [] 
        
        res, queue = [], __import__('collections').deque([(root, "")]) # store node and path at the same time 
        while queue: 
            node, path = queue.popleft() 
            if not node.left and not node.right: 
                res.append(path + str(node.val)) # leaf add past path and its value 
                
            if node.left: 
                queue.append((node.left, path + str(node.val) + '->')) 
                # left first in 
            if node.right: 
                queue.append((node.right, path + str(node.val) + '->')) 
                # right last in 
        return res 