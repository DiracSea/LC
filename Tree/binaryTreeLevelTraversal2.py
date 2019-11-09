# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        # reverse bfs
        if not root: return [] 
        ans = []
        queue = deque([root]) 
        
        while queue: 
            level, size = [], len(queue) 
            
            for _ in range(size): 
                node = queue.popleft() 
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
                level.append(node.val) 
            ans.append(level) 
        return reversed(ans)

    def levelOrderBottom1(self, root: TreeNode):
        # dfs 
        if not root: return [] 
        ans = [] 
        self.dfs(ans, root, 0)
        return ans[::-1]
    
    def dfs(self, ans, node, level): 
        if not node: return 
        if level >= len(ans): 
            ans.append([]) 
        
        ans[level].append(node.val) 
        if node.left: 
            self.dfs(ans, node.left, level+1) 
        if node.right: 
            self.dfs(ans, node.right, level+1) 