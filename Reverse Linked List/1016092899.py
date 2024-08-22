# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
            
        ls = []

        cur = head
        while cur != None:
            ls.append(cur)
            cur = cur.next

        for i in range(len(ls)-1, -1, -1):
            ls[i].next = ls[i-1]
        
        ls[0].next = None

        return ls[len(ls)-1]

