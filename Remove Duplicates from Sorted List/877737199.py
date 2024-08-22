# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        prev = head
        hashtable = {}
        
        while curNode != None:
            if hashtable.get(curNode.val) == None:
                hashtable[curNode.val] = 1
                prev = curNode
            else:
                # need to remove curNode as this is already in table
                prev.next = curNode.next 
            
            curNode = curNode.next

        return head