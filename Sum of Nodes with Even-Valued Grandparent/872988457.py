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
                grandparent = True

            if node.left != None:
                queue.append(node.left)

                if grandparent:
                    if node.left.left != None:
                        sum += node.left.left.val
                    if node.left.right != None:
                        sum += node.left.right.val
             
            if node.right != None:
                queue.append(node.right)

                if grandparent:
                    if node.right.left != None:
                        sum += node.right.left.val
                    if node.right.right != None:
                        sum += node.right.right.val

            grandparent = False 

        return sum