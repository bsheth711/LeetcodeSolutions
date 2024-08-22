"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return None

            if node.val in visited:
                return visited[node.val]
    
            new = Node(node.val)

            visited[node.val] = new
    
            for n in node.neighbors:
                child = dfs(n)
                new.neighbors.append(child) 

            return new
        
        return dfs(node)