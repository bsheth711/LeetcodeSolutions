# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        l3 = ListNode(0)
        dummy = l3

        while l1 or l2 or carry:
            total = 0

            if l1: 
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry:
                total += 1
                carry = False
            
            if total >= 10:
                total = total % 10
                carry = True
            
            l3.next = ListNode(total)
            l3 = l3.next
        
        return dummy.next
            

