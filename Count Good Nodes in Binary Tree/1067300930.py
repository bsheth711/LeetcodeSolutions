# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0 


        def dfs(root, cur=-math.inf):
            nonlocal count

            if not root:
                return
            
            if root.val >= cur:
                cur = root.val
                count += 1
            
            if root.left:
                dfs(root.left, cur)

            if root.right:
                dfs(root.right, cur)
            
        
        dfs(root)

        return count