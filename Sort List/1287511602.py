# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head:
            return None

        ls = []

        cur = head

        while cur != None:
            ls.append(cur)
            cur = cur.next
        
        ls.sort(key=lambda x: x.val)

        prev = None
        for node in reversed(ls):
            node.next = prev
            prev = node
        
        newHead = ls[0]

        return newHead