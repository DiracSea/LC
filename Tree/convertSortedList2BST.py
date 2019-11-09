# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursion and fast-slow pointer
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        # slow is 1x, fast is 2x, when fast reach the end, slow in the mid
        slow, fast = head, head.next.next
        while fast and fast.next: # even and odd
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next # middle
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
        
    # conversion to array
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        values = self.mapListToValues(head) 
        
        def dfs(l, r): 
            if l > r: return None 
            mid = (l+r)//2 
            node = TreeNode(values[mid]) 
            node.left = dfs(l, mid-1) 
            node.right = dfs(mid+1, r) 
            return node
        
        return dfs(0, len(values)-1)
                
    def mapListToValues(self, head): 
        vals = [] 
        while head: 
            vals.append(head.val) 
            head = head.next 
        return vals 

    # inorder 
    # three is subtree
    def sortedListToBST(self, head: 'ListNode') -> 'TreeNode':
        size = self.findSize(head) 
        
        def dfs(l, r): 
            nonlocal head 
            if l < r: 
                return None 
            mid = (l+r)//2 
            l = dfs(l, mid-1) 
            node = TreeNode(head.val) 
            node.left = l
            head = head.next 
            
            node.right = dfs(mid+1, r) 
            return node
        
        return dfs(0, size-1)
                
    def findSize(self, head): 
        ptr = head 
        c = 0 
        while ptr: 
            ptr = ptr.next 
            c += 1 
        return c 