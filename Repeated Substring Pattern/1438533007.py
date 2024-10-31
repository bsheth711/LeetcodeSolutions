class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        offset = 1

        while offset < (len(s) // 2) + 1: 

            if self.helper(s, offset):
                return True

            offset += 1

        return False
    
    def helper(self, s, offset):

        for i in range(len(s)):
            if s[i] != s[(i + offset) % len(s)]:
                return False

        return True

