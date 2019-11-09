"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    
    def levelOrder(self, root: 'Node'):
        # bfs 
        if not root: return [] 
        res = [] 
        queue = deque([root]) 
        
        while queue: 
            cur_level, size = [], len(queue) 
            for _ in range(size): 
                node = queue.popleft() 
                
                for n in node.children: 
                    queue.append(n) 
                cur_level.append(node.val) 
                
            res.append(cur_level) 
        return res 

    def levelOrder1(self, root: 'Node'):
        # dfs 
        if not root: return [] 
        res = []
        self.dfs(res, root, 0) 
        return res 
        
    def dfs(self, res, node, level): 
        if level >= len(res): 
            res.append([]) 
            
        for n in node.children: 
            self.dfs(res, n, level+1) 
            
        res[level].append(node.val)