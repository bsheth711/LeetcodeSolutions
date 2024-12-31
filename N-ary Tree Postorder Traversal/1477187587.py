"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        ret = []

        def dfs(node):
            nonlocal ret

            for child in node.children:
                dfs(child)
            
            ret.append(node.val)
        
        dfs(root)

        return ret
        