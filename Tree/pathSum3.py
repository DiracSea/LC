# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 
class Solution:
     
    def pathSum(self, root: 'TreeNode', s: int) -> int:
        # dfs*2 
        # define global return var 
        # 1st layer dfs to go through each node 
        global numOfPaths
        numOfPaths = 0
        self.dfs(root, s) 
        # return res 
        return numOfPaths 
    
    # 1st traverse through tree 
    def dfs(self, node, s): 
        if not node: return 
        
        # dfs break down 
        self.test(node, s) # find target from this node
        self.dfs(node.left, s) 
        self.dfs(node.right, s) 
        
    # 2nd for given node, dfs find path 
    def test(self, node, s): 
        if not node: return 
        
        if node.val == s: 
            global numOfPaths 
            numOfPaths += 1 
        
        self.test(node.left, s - node.val) 
        self.test(node.right, s - node.val)

    def pathSum1(self, root, s): 
        global res 
        res = 0 
        cache = {0:1} 
        self.dfs1(root, s, 0, cache) 
        
        return res 
    
    def dfs1(self, node, s, curPathSum, cache): 
        if not node: return 
        # cal curPathSum and require oldPathSum 
        curPathSum += node.val 
        oldPathSum = curPathSum - s 
        
        # updata res and cache 
        global res 
        res += cache.get(oldPathSum, 0) # if there is oldPathSum exists, there is a res 
        cache[curPathSum] = cache.get(curPathSum, 0) + 1 # store the curPathSum, they become old Path
        
        # dfs breakdown 
        self.dfs1(node.left, s, curPathSum, cache) 
        self.dfs1(node.right, s, curPathSum, cache) 
        
        # when move to dif branch, del curPathSum
        cache[curPathSum] -= 1 