class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        expressions = 0 

        def dfs(i, cur):
            nonlocal expressions

            if (i, cur) in memo:
                expressions += memo[(i, cur)] 
                return memo[(i, cur)]

            if i == len(nums):
    
                if cur == target:
                    expressions += 1 

                    return 1
                    
                return 0

            
            waysToEnd = dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])

            memo[(i, cur)] = waysToEnd

            return memo[(i, cur)]
        
        dfs(0, 0)
        
        return expressions

            

            
            
