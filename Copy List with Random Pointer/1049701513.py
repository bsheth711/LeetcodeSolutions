"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        table = {}
        
        cur = head
        while cur:
            table[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            table[cur].next = table[cur.next] if cur.next else None
            table[cur].random = table[cur.random] if cur.random else None
            cur = cur.next

        return table[head]



        