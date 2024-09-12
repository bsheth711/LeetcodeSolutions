class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [n] * n
        dp[0] = 0

        for i in range(1, n):

            for coin in coins:
                if i - coin < 0 or dp[i - coin] == n:
                    continue

                dp[i] = min(dp[i - coin] + 1, dp[i])


        return dp[amount] if dp[amount] != n else -1

        