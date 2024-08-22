# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append(root)
        counter = 1

        if not root:
            return 0

        while q:

            newNodes = []
            for _ in range(len(q)):
                node = q.pop()

                if not node.left and not node.right:
                    return counter
                
                if node.left:
                    newNodes.append(node.left)
                
                if node.right:
                    newNodes.append(node.right)
                
            q.extend(newNodes)

            counter += 1
        
        return counter

        