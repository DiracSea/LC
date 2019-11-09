# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque # bi queue
class Solution:
    def levelOrder(self, root: 'TreeNode'):
        # BFS iterative
        if not root: return [] 
        queue, res = deque([root]), [] 
        
        while queue: 
            cur_level, size = [], len(queue) 
            for _ in range(size): # size is the number of nodes in each layer 
                node = queue.popleft() 
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
                cur_level.append(node.val) 
            res.append(cur_level) 
        return res 

    def levelOrder1(self, root: 'TreeNode'):
        # DFS recursive
        res = [] 
        self.helper(res, root, 0) 
        return res 
    
    def helper(self, res, node, height): 
        if not node: return 
        if height >= len(res): 
            res.append([]) 
        
        res[height].append(node.val) 
        self.helper(res, node.left, height+1) 
        self.helper(res, node.right, height+1) 
            