class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, remaining):
            if len(cur) == len(nums):
                res.append(cur)
                return

            for i in range(len(remaining)):
                cpy = remaining.copy() 
                new = cur.copy()
                removed = cpy.pop(i)
                new.append(removed)
                dfs(new, cpy)
        
        dfs([], nums)
        
        return res

