# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        if not nums: return None 
        mid = (len(nums)-1)//2 
        root = TreeNode(nums[mid]) 
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:]) # mid + 1
        
        return root 

    def sortedArrayToBST1(self, nums: 'List[int]') -> 'TreeNode':
        self.nums = nums
        return self.dfs(0,len(nums)-1)
    
    def dfs(self,l,r):
        if l > r:
            return None
        mid = (l+r)//2
        node = TreeNode(self.nums[mid])
        node.left = self.dfs(l,mid-1)
        node.right = self.dfs(mid+1,r)
        return node       
                