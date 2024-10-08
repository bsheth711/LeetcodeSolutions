# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)        

    
    def isSame(self, rootA, rootB):
        if not rootA and not rootB:
            return True

        if rootA and rootB and rootA.val == rootB.val: 
            return self.isSame(rootA.left, rootB.left) and self.isSame(rootA.right, rootB.right)
        
        return False
 