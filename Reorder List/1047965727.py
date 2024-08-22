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

        slow = head
        fast = head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half 
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



        '''
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
        '''