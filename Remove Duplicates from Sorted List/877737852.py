# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prev = head
        seen = set()
        
        while curNode != None:
            if curNode.val in seen:
                prev.next = curNode.next 
            else:
                seen.add(curNode.val)
                prev = curNode
            
            curNode = curNode.next

        return head