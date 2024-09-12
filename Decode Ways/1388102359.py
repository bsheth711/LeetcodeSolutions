class Solution:
    def numDecodings(self, s: str) -> int:
        doubleDigits = set(range(10, 27))
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1

        for i in range(1, len(s)):
            first = int(s[i])
            second = int(s[i - 1: i + 1])

            if first != 0:
                dp[i + 1] += dp[i]
            if second in doubleDigits:
                dp[i + 1] += dp[i - 1] 

        return dp[-1]