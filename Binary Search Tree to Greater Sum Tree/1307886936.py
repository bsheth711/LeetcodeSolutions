# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curVal = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root

    def dfs(self, node):

        if node.right:
            self.dfs(node.right)
        
        print(f'node.val {node.val}, new {node.val + self.curVal}')
        node.val += self.curVal
        self.curVal = node.val

        if node.left:
            self.dfs(node.left)
        
        return node.val


        

        

        



        