class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s * 2
        return s in t[1:-1] 

