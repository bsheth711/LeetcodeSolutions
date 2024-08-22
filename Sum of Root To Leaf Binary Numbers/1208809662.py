# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        ls = []
        ls.append(root.val)

        def dfs(cur):
            nonlocal ans
            nonlocal ls

            if not cur.left and not cur.right:
                ans += self.calc(ls)
                return
            
            if cur.left:
                ls.append(cur.left.val)
                dfs(cur.left)
                ls.pop()
            
            if cur.right:
                ls.append(cur.right.val)
                dfs(cur.right)
                ls.pop()
        
        dfs(root)

        return ans
    
    def calc(self, ls):
        place = 1
        total = 0

        for i in reversed(ls):
            total += place * i
            place *= 2
        
        return total


            
