# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        self.dfs(root, ls)
        return ls

    def dfs(self, node, ls):
        if not node:
            return

        if node.left:
            self.dfs(node.left, ls)
        
        ls.append(node.val)

        if node.right != None:
            self.dfs(node.right, ls)

