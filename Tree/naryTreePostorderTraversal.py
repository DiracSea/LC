"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node'): 
        ans = [] 
        if root: 
            self.traversal(root, ans)
        return ans 
        
    def traversal(self, node, ans): 
        for n in node.children: 
            self.traversal(n, ans) 
        ans.append(node.val)

    def postorder1(self, root: 'Node'): 
        # iteratively 
        if not root: 
            return [] 
        ans = [] 
        stack = [(root, False)]
        while stack: 
            node, visited = stack.pop() 
            if visited: 
                ans.append(node.val) 
            else: 
                stack.append((node, True)) # put root in the end
                for n in node.children[::-1]: 
                    stack.append((n, False))
                
        return ans 

    def postorder2(self, root: 'Node'): 
        # iteratively 
        '''
          1            3
           \    ->      \
        3 - 2        1 - 2
        ''' 
        if not root: return []
        stack = [root] 
        res = [] 
        while stack: 
            node = stack.pop() 
            
            for n in node.children: 
                stack.append(n) 
            res.append(node.val) 
            
        return reversed(res)