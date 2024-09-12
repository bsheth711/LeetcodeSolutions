class Solution:
    def numDecodings(self, s: str) -> int:
        doubleDigits = set(range(10, 27))
        dp = [0] * (len(s) + 1)

        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1):
            first = int(s[i - 1: i])
            second = int(s[i - 2: i])

            if first != 0:
                dp[i] += dp[i - 1]
            if second in doubleDigits:
                dp[i] += dp[i - 2] 

        return dp[-1]