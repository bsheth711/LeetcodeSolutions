class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def step(cur, i):
            if i == len(nums):
                res.append(cur.copy())
                return 

            cur.append(nums[i])
            step(cur, i + 1)
            cur.pop()

            prev = nums[i]
        
            while i < len(nums) and nums[i] == prev:
                i += 1
            
            step(cur, i)
        
        step([], 0)

        return res
            

