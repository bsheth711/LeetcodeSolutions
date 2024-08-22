# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        N = 39847393849
        ret = None

        cur = headA
        while cur:
            cur.val *= N
            cur = cur.next
        
        cur = headB
        while cur:
            if cur.val % N == 0:
                ret = cur
                break
            cur = cur.next

        cur = headA
        while cur:
            cur.val //= N
            cur = cur.next
  
        return ret
