# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        parents[root.val] = root
        self.addParents(root, parents)

        pVisited = set()
        qVisited = set()
        pAncestor = p
        qAncestor = q

        while True:
            if pAncestor == qAncestor:
                return pAncestor
            if pAncestor in qVisited:
                return pAncestor
            if qAncestor in pVisited:
                return qAncestor
            
            pVisited.add(pAncestor)
            qVisited.add(qAncestor)

            pAncestor = parents[pAncestor.val]
            qAncestor = parents[qAncestor.val]

    def addParents(self, node, parents):
        if node == None:
            return
        
        if node.left != None:
            parents[node.left.val] = node
            self.addParents(node.left, parents)

        if node.right != None:
            parents[node.right.val] = node
            self.addParents(node.right, parents)
