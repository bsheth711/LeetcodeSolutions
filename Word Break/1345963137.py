class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):

            for word in wordDict:
                if i + 1 < len(word):
                    continue 
                
                dp[i] = dp[i] or ((i == len(word) - 1 or dp[i - len(word)]) and s[i - len(word) + 1: i + 1] == word)
                
                '''
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                '''
        

        return dp[-1]


        