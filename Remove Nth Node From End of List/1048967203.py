# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # idea: create trailing pointer that trails n nodes behind

        cur = head
        while n > 0:
            cur = cur.next
            n -= 1
       
        prev = None
        trailing = head
        while cur:
            prev = trailing
            trailing = trailing.next
            cur = cur.next

        if not prev:
            return trailing.next

        prev.next = trailing.next
        trailing.next = None

        return head