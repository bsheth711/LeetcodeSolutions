class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        cur = 0
        for c in t:
            cur += (c == s[cur])

            if cur >= len(s):
                break
        
        
        if cur == len(s):
            return True
        
        return False
 