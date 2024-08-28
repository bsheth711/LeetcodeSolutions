# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(next = head)
        cur = dummy

        while cur.next and cur.next.next:
            a = cur.next
            b = cur.next.next

            a.next = b.next
            cur.next = b
            b.next = a

            cur = cur.next.next

        
        return dummy.next
        