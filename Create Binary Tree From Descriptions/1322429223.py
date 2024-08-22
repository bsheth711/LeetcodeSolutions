# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        lookup = {}
        childNodes = set()
        rootNode = set()
        counts = {}

        for parent, child, left in descriptions:
            if parent not in childNodes:
                rootNode.add(parent)
            childNodes.add(child)
            rootNode.discard(child)

            if parent not in lookup:
                lookup[parent] = TreeNode(parent)
            
            if child not in lookup:
                lookup[child] = TreeNode(child)

            if left == 1:
                lookup[parent].left = lookup[child]
            else:
                lookup[parent].right = lookup[child]
        
        return lookup[rootNode.pop()]
        