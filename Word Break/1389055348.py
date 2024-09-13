class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):

            for word in wordDict:
                if i - len(word) < 0:
                    continue
                if s[i - len(word): i] == word and dp[i - len(word)]:
                    dp[i] = True
                    break

        return dp[-1]
        