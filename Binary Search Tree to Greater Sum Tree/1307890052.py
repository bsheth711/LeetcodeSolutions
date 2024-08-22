# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curVal = 0

        def dfs(node):
            nonlocal curVal
    
            if node.right:
                dfs(node.right)
            
            node.val += curVal
            curVal = node.val
    
            if node.left:
                dfs(node.left)
            
            return node.val

        dfs(root)
        return root


        

        

        



        