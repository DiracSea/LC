# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque 
class Solution:
    def rightSideView(self, root):
        if not root: return [] 
        res, queue = [], deque([root])
        
        while queue: 
            size, flag = len(queue), 1 
            for _ in range(size):  
                if flag: 
                    res.append(queue[-1].val) 
                    flag = 0 
                node = queue.popleft() 
                
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
                
        return res 
            

    # optimization  
    def rightSideView(self, root):
        if not root: return [] 
        res, queue = [], deque([root])
        
        while queue:  
            for _ in range(len(queue)):  
                node = queue.popleft() 
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
            res.append(node.val) # the last node 
                
        return res 

    def rightSideView2(self, root):
        # dfs  
        # 先递归右，后递归左，记录一个深度，当进入新的一层深度，将当前root.val放入return数组里。
        self.res = []
        if not root: return [] 
        self.dfs(root, 1) 
        return self.res 

    def dfs(self, node, depth): 
        if not node: return 
        if len(self.res) < depth: 
            self.res.append(node.val) 
        if node.right: 
            self.dfs(node.right, depth+1) 
        if node.left: 
            self.dfs(node.left, depth+1) 
                