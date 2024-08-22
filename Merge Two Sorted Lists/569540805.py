# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        prev = None
        root = None
    
        def appendList(tail, prev, list):
            while (list != None):
                prev = tail
                tail = list
                list = list.next
                if (prev != None):
                    prev.next = tail
            
        
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        
        while(True):
            prev = l3
            
            if (l1.val <= l2.val):
                l3 = l1
                l1 = l1.next
                if (prev != None):
                    prev.next = l3
                else:
                    root = l3
            
                if (l1 == None):
                    appendList(l3, prev, l2)
                    return root
            else:
                l3 = l2
                l2 = l2.next 
                if (prev != None):
                    prev.next = l3
                else:
                    root = l3
            
                if (l2 == None):
                    appendList(l3, prev, l1)
                    return root
        
        