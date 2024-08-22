# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curNode = head
        prev = None

        # change list to be double linked
        while curNode != None:
            curNode.prev = prev
            prev = curNode
            curNode = curNode.next

        curNode = prev
        counter = 1
        
        # remove nth node from end
        while curNode != None:
            if counter == n:
                if curNode.prev == None:
                    head = curNode.next
                else:
                    curNode.prev.next = curNode.next

                if curNode.next != None:
                    curNode.next.prev = curNode.prev
                
                break
                    
            curNode = curNode.prev
            counter += 1
        
        return head