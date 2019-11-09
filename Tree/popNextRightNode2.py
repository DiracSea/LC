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

    def connect1(self, root: 'Node') -> 'Node':
        # O1 
        node = root 
        tail = dummy = Node(0) 
        while node: 
            tail.next = node.left # left child
            if tail.next: 
                tail = tail.next
                
            tail.next = node.right # right child 
            if tail.next: 
                tail = tail.next 
                
            node = node.next # next node
            if not node: # next line
                tail = dummy # next line zero
                node = dummy.next # next line first
        return root