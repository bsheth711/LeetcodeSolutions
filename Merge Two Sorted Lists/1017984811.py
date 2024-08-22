# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Special case where one of the lists is empty:
        #   return the other list (if both are empty then it doesn't matter)
        if not list1:
            return list2
        elif not list2:
            return list1
        
        # Find out what node will be the head of the new list to save for later
        head = None
        curLeft = list1
        curRight = list2

        if curLeft.val < curRight.val:
            head = curLeft
            curLeft = curLeft.next
        else:
            head = curRight
            curRight = curRight.next
        
        prev = head

        # Append the min between the current lists. Increment the iterator for the list chosen. 
        while curLeft and curRight:
            if curLeft.val < curRight.val:
                prev.next = curLeft
                curLeft = curLeft.next
                prev = prev.next
            else:
                prev.next = curRight
                curRight = curRight.next
                prev = prev.next
        
        # If one of the lists is not completely exhausted then append the rest
        if curLeft:
            prev.next = curLeft
        elif curRight:
            prev.next = curRight

        return head
