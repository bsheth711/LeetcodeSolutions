# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def DFS(node, depth):               
            nonlocal maxDepth

            if node == None:
                return

            if depth > maxDepth:
                maxDepth = depth
 
            if node.left != None:
                DFS(node.left, depth+1)

            if node.right != None:
                DFS(node.right, depth+1)
        
        DFS(root, 1)

        return maxDepth