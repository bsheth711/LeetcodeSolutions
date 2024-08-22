# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        first = None
        last = None

        while True:
            min = sys.maxsize
            idx = None
            toRemove = None
    
            for i, node in enumerate(lists):
                if node == None:
                    continue

                if node.val < min:
                    min = node.val
                    toRemove = node
                    idx = i
            
            if toRemove == None:
                break

            if first == None:
                first = toRemove
            else:
                last.next = toRemove 

            lists[idx] = toRemove.next
            last = toRemove

        return first
        