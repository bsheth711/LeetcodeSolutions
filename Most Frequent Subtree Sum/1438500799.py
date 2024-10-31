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

        counts = [(-sums[val], val) for val in sums]
        counts.sort()

        return [val for (count, val) in counts if count == counts[0][0]]



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
