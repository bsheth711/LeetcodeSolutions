# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
    
    def dfs(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        
        if l.val != r.val:
            return False
        
        outside = self.dfs(l.left, r.right)
        inside = self.dfs(l.right, r.left)

        return outside and inside