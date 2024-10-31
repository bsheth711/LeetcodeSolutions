# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sums = defaultdict(int)

        self.dfs(root, sums)

        best = 0

        for val in sums:
            best = max(best, sums[val])

        ret = []

        for val in sums:
            if sums[val] == best:
                ret.append(val)
        
        return ret


    def dfs(self, node, sums):
        if not node.left and not node.right:
            sums[node.val] += 1
            return node.val
        
        left = 0
        if node.left:
            left = self.dfs(node.left, sums)
            
        right = 0
        if node.right:
            right = self.dfs(node.right, sums) 

        total = left + right + node.val
        sums[total] += 1

        return total 
