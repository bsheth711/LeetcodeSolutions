class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        n = amount + 1
        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):

            best = n

            for coin in coins:
                if i - coin < 0 or dp[i - coin] == -1:
                    continue

                best = min(dp[i - coin] + 1, best)

            if best != n:
                dp[i] = best

        return dp[amount] if dp[amount] > 0 else -1

        