# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not(root.val > self.dfs(root.left, False)):
            return False
        
        if not(root.val < self.dfs(root.right, True)):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def dfs(self, root, wantMin):
        if not root:
            if wantMin:
                return math.inf
            else:
                return -math.inf

        if not root.left and not root.right:
            return root.val
        
        l = self.dfs(root.left, wantMin)
        
        r = self.dfs(root.right, wantMin)

        if wantMin:
            return min(l, r, root.val) 
        
        return max(l, r, root.val)