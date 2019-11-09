# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs 
        if not root: return [] 
        res, queue = [], deque([root]) 
        depth = 0 
        
        while queue: 
            layer, size = [], len(queue) 
            for _ in range(size): 
                node = queue.popleft() 
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
                layer.append(node.val)
            if depth&1: 
                res.append(layer[::-1])
            else: 
                res.append(layer)
            depth += 1 
        return res 

    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        # dfs 
        if not root: return [] 
        res = [] 
        self.dfs(res, root, 0) 
        return res 
    
    def dfs(self, res, node, level): 
        if not node: return 
        if level >= len(res): 
            res.append([]) 
        if level&1: 
            res[level] = [node.val] + res[level] 
        else: 
            res[level] += [node.val] 
        if node.left: 
            self.dfs(res, node.left, level+1) 
        if node.right: 
            self.dfs(res, node.right, level+1)