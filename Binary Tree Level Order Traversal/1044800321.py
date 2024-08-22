# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ret = []

        q = Queue()
        q.put(root)

        while not q.empty():
            ls = []

            for i in range(q.qsize()):
                cur = q.get()
                ls.append(cur.val)

                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            
            if ls:
                ret.append(ls)
             
        return ret


        