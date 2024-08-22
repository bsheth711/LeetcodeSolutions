# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        cur = head
        total = deque()

        while cur:
            total.append(cur)
            cur = cur.next

        last = head
        i = 0
        while total:
            if i % 2:
                tmp = total.pop()
            else:
                tmp = total.popleft()
            
            last.next = tmp 
            last = tmp
            i += 1
        
        last.next = None