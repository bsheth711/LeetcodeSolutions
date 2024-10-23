"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ls = []

        self.dfs(root, ls)

        return ls
    
    def dfs(self, node, ls):
        if not node:
            return
        
        ls.append(node.val)
        
        for child in node.children:
            self.dfs(child, ls)

        