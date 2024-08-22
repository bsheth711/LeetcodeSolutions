# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = {}

        def dfs(root, depth = 0):
            nonlocal levels

            if not root:
                return
            
            levels[depth] = root.val
            
            if root.left:
                dfs(root.left, depth+1)
            
            if root.right:
                dfs(root.right, depth+1)
        
        dfs(root)

        ans = []

        for level in levels:
            ans.append(levels[level])

        return ans
