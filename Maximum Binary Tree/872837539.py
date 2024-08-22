# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # finding argmax
        maxIdx = 0
        max = 0
        for i, num in enumerate(nums):
            if num > max:
                maxIdx = i
                max = num

        prefix = nums[:maxIdx]
        suffix = nums[maxIdx + 1:]

        node = TreeNode(max)

        if len(prefix) != 0:
            left = self.constructMaximumBinaryTree(prefix)
            node.left = left
       
        if len(suffix) != 0:
            right = self.constructMaximumBinaryTree(suffix)
            node.right = right

        return node

