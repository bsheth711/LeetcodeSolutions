# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 2 pass algo
        if not head:
            return None

        length = 1

        cur = head
        
        while cur.next:
            length += 1
            cur = cur.next

        last = cur
        remainder = k % length

        if length <= 1 or remainder == 0:
            return head

        cur = head
        for i in range(length - remainder - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        last.next = head

        return newHead
            

