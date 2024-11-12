class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @cache
        def dfs(i, cur):

            if i == len(nums):
    
                if cur == target:
                    return 1
                    
                return 0
            
            return  dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])
        
        return dfs(0, 0)

            

            
            
