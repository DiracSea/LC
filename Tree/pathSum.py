# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', s: int) -> bool:
        # dfs + stack 
        if not root: # root is None, s is 0 return False 
            return False 
        
        stack = [(root, root.val)]
        while stack: 
            node, value = stack.pop() 
            if not node.left and not node.right: 
                if value == s: return True 
            if node.right: 
                stack.append((node.right, value + node.right.val)) 
            if node.left: 
                stack.append((node.left, value + node.left.val)) 
        return False 

    def hasPathSum1(self, root: 'TreeNode', s: int) -> bool:
        # bfs + queue 
        if not root: return False 
        
        queue = __import__('collections').deque([(root, root.val)])
        while queue: 
            node, value = queue.popleft() 
            if not node.right and not node.left: 
                if value == s: return True 
            if node.left: 
                queue.append((node.left, node.left.val + value)) 
            if node.right: 
                queue.append((node.right, node.right.val + value)) 
        
        return False 