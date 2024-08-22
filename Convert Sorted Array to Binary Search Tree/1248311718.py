# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.helper(nums, 0, len(nums))

    
    def helper(self, nums, l, r):
        if l == r:
            return None

        mid = (l + r) // 2
        parent = TreeNode(nums[mid])
        parent.left = self.helper(nums, l, mid)
        parent.right = self.helper(nums, mid + 1, r)
        return parent

