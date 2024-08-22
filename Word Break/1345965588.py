class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):

            for word in wordDict:
                
                dp[i] = dp[i] or (i + 1 >= len(word) and ((i == len(word) - 1 or dp[i - len(word)]) and s[i - len(word) + 1: i + 1] == word)) 

        return dp[-1]


        