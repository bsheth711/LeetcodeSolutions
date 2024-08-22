"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = deque()
        q.append(root)

        while q:

            toExtend = []
            last = None
            for _ in range(len(q)):
                cur = q.popleft()

                try:
                    last.next = cur
                except:
                    pass
                
                if cur.left:
                    toExtend.append(cur.left)
                if cur.right:
                    toExtend.append(cur.right)
                
                last = cur
            
            q.extend(toExtend)
        
        return root

