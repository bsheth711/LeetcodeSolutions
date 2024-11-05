# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter()
        q = deque()
        q.append(root)

        while q:

            for _ in range(len(q)):
                cur = q.popleft()

                counts[cur.val] += 1

                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
        
        best = 0

        for val in counts:
            best = max(best, counts[val])
        
        return [val for val in counts if counts[val] == best]

                
