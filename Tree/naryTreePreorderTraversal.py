"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node'):
        ans = [] 
        if root: 
            self.traverse(root, ans) 
        return ans 
    
    def traverse(self, node, ans): 
        if node: 
            ans.append(node.val) 
            for n in node.children: 
                self.traverse(n, ans)

    def preorder1(self, root: 'Node'):
        # iteratively 
        ans = [] 
        if root: 
            stack = [root] 
            while stack: 
                node = stack.pop() 
                ans.append(node.val) 
                for n in node.children[::-1]: 
                    stack.append(n)
        return ans 