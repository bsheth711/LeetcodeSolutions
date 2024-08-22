# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curNode = head
        ls = []

        while curNode != None:
            ls.append(curNode)
            curNode = curNode.next

        toRemove = ls[len(ls) - n]

        # special case: first node
        if len(ls) - n == 0:
            head = toRemove.next
        # all other nodes
        else:
            prev = ls[len(ls) - 1 - n]
            prev.next = toRemove.next
        
        return head