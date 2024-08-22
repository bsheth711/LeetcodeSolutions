# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.dfs(root, ans)
        return ans
    
    def dfs(self, node, ans):
        if node == None:
            return None

        ans.append(node.val)

        if node.left != None:
            self.dfs(node.left, ans)

        if node.right != None:
            self.dfs(node.right, ans)