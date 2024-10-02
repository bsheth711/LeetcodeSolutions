# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        best = sys.maxsize
    
        def dfs(node):
            nonlocal best

            
            if not node.left and not node.right:
                return (node.val, node.val) 

            lowestInSubtree = node.val
            highestInSubtree = node.val

            if node.left:
                leftMinMax = dfs(node.left)
                lowestInSubtree = leftMinMax[0]
                best = min(best, abs(node.val - leftMinMax[1]))
            
            if node.right:
                rightMinMax = dfs(node.right)
                highestInSubtree = rightMinMax[1]
                best = min(best, abs(node.val - rightMinMax[0]))

            
            return (lowestInSubtree, highestInSubtree)

        dfs(root)

        return best