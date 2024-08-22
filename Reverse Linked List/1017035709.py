# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        prev = None
        cur = head
        while cur != None:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp

        return prev

