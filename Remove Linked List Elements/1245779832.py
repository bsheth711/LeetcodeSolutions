# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        prev = ListNode(next = head)
        dummy = prev

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next

            cur = cur.next

        return dummy.next
        