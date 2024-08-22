# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        sum = 0
        grandparent = False

        while len(queue) != 0:
            node = queue.popleft()
        
            if node.val % 2 == 0:
                sum += self.dfs(node)

            if node.left != None:
                queue.append(node.left)
             
            if node.right != None:
                queue.append(node.right)

            grandparent = False 

        return sum

    def dfs(self, node, sum=0, depth=2):

        if node.left != None:
            sum = self.dfs(node.left, sum, depth-1)

        if node.right != None:
            sum = self.dfs(node.right, sum, depth-1)

        if depth == 0:
            sum += node.val

        return sum
        