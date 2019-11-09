# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # inorder
    # flatten 
    def __init__(self, root: TreeNode):
        self.nodes_sorted = [] # all node
        self.idx = -1 # pointer to the next smallest element
        self.inorder(root)
        
    def inorder(self, root): 
        if not root: return 
        self.inorder(root.left) 
        self.nodes_sorted.append(root.val) 
        self.inorder(root.right)

    def next(self) -> int: # O1 means should have list
        """
        @return the next smallest number
        """
        self.idx += 1 
        return self.nodes_sorted[self.idx]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.idx + 1 < len(self.nodes_sorted)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class BSTIterator1:
    # inorder
    # controlled cursion
    def __init__(self, root: TreeNode):
        # stack for the recursion simulation
        self.stack = [] 
        
        self.leftmost_inorder(root)
        
    def leftmost_inorder(self, root): 
        while root: 
            self.stack.append(root) 
            root = root.left

    def next(self) -> int: # O1 means should have list
        """
        @return the next smallest number
        """
        # node at the top is the next smallest
        topmost_node = self.stack.pop() 
        if topmost_node.right: 
            self.leftmost_inorder(topmost_node.right) 
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0