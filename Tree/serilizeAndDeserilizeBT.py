# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    # dfs
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node): 
            if node: 
                vals.append(str(node.val)) 
                dfs(node.left) 
                dfs(node.right) 
                
            else: 
                vals.append('#') 
        vals = [] 
        dfs(root) 
        return ' '.join(vals) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(): 
            val = next(vals) # iter 
            if val == '#': return None 
            node = TreeNode(int(val)) 
            node.left = dfs() 
            node.right = dfs() 
            return node 
        
        vals = iter(data.split()) 
        return dfs()
            
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
from collections import deque
class Codec1:
    # bfs
    # best
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = [] 
        queue = deque([root]) 
        while queue: 
            node = queue.popleft() 
            res.append(str(node.val) if node else 'null') 
            if node: 
                queue.append(node.left) 
                queue.append(node.right) 
                
        while res and res[-1] == 'null': 
            res.pop() 
        return '[' + ','.join(res) + ']'
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def walk(n, i): 
            if i >= n or data[i] == 'null' or data[i] == '': 
                return None
            node = TreeNode(data[i] if data[i] != '' else '') 
            node.left = walk(n, 2*i+1) 
            node.right = walk(n, 2*i+2) 
            return node 
        data = data[1:-1].split() 
        return walk(len(data), 0)
        