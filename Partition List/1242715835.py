# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # iterate throught list
        # for each node add it to left list if < x or right list if >= x
        if not head:
            return None

        cur = head
        lHead = ListNode(-1)
        rHead = ListNode(-1)
        lList = lHead
        rList = rHead

        while cur:
            if cur.val < x:
                lList.next = cur
                lList = lList.next
            else:
                rList.next = cur
                rList = rList.next

            cur = cur.next
        
        rList.next = None
        lList.next = rHead.next

        return lHead.next