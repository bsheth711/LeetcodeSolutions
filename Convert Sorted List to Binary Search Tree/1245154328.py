# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. find midpoint of list
        # 2. recursively place left and right portions of list
        if head == None:
            return None
        return self.helper(head, None)
        
    def helper(self, start, end):
        slow = start
        fast = start

        if start == end:
            return None
        
        while fast != end and fast.next != end:
            fast = fast.next.next
            slow = slow.next
        
        node = TreeNode(slow.val)
        node.left = self.helper(start, slow)
        node.right = self.helper(slow.next, end)
        return node