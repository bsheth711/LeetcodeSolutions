class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]: 
        res = []
        cur = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(cur[::])
                return

            # choosing to add i
            cur.append(nums[i])
            dfs(i + 1)

            # choosing to not add i
            cur.pop()
            n = nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 
            dfs(i + 1)

        dfs(0) 

        return res