# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root) -> bool:
        return self.check(root) != -1 
    
    # postorder
    def check(self, node): 
        if not node: return 0 
        left = self.check(node.left) 
        if left == -1: 
            return -1
        right = self.check(node.right) 
        if right == -1: 
            return -1 
        if abs(left - right) > 1: # unbalance
            return -1 
        return 1 + max(left, right) # depth 
    
    # iterative
    def isBalanced1(self, root) -> bool:
        stack, node, last, depths = [], root, None, {} 
        while stack or node: 
            if node: 
                stack.append(node) 
                node = node.left 
            
            else: 
                node = stack[-1] 
                if not node.right or last == node.right: 
                    node = stack.pop() 
                    left, right = depths.get(node.left, 0), depths.get(node.right, 0) 
                    if abs(left - right) > 1: return False 
                    depths[node] = 1 + max(left, right) 
                    last = node 
                    node = None 
                
                else: 
                    node = node.right 
        
        return True

'''
    def isBalanced2(self, root):
        self.isBalanced2 = True
        self.getHeight(root)
        return self.isBalanced2
        
    
    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1: 
            self.isBalanced2 = False
        return max(left, right) + 1
        
'''