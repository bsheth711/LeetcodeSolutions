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
        # val: node

        cur = head
        while cur:
            table[cur] = Node(cur.val)
            cur = cur.next
        
        for node in table:
            print(table[node].val)


        cur = head
        while cur:
            if cur.next:
                table[cur].next = table[cur.next]

            if cur.random:
                table[cur].random = table[cur.random]
            else:
                table[cur].random = None

            cur = cur.next

        return table[head]



        