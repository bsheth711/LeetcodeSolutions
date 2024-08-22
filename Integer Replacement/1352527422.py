class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        memo[1] = 0
        memo[2] = 1
        
        return self.helper(memo, n)
    
    def helper(self, memo, n):
        if n in memo:
            return memo[n]

        if n % 2 == 0:
            memo[n] = self.helper(memo, n // 2) + 1
        else: 
            memo[n] = min(self.helper(memo, n + 1), self.helper(memo, n - 1)) + 1

        return memo[n]