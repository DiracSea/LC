"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque 
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bfs 
        if not root: return 
        queue = deque([root]) 
        while queue: 
            size = len(queue)
            node, prev = None, None 
            for _ in range(size): 
                node = queue.popleft() 
                if prev: 
                    prev.next = node
                prev = node 
                
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right) 
                
            prev.next = None 
            
        return root 

    def connect1(self, root): 
        # ite O1 space
        node = root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return node

    def connect2(self, root: 'Node') -> 'Node':
        # O1 space rec
        if not root or not root.left: return root 
        
        root.left.next = root.right 
        if root.next: 
            root.right.next = root.next.left 
        
        if root.left: 
            self.connect(root.left) 
        if root.right: 
            self.connect(root.right) 
        
        return root 