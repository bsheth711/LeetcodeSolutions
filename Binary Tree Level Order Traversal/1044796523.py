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

            while not q.empty():
                ls.append(q.get())
            
            toAdd = []
            for cur in ls:
                toAdd.append(cur.val)
    
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
            
            if toAdd:
                ret.append(toAdd)
            
            
        return ret


        