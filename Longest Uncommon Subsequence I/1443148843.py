class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
            
        if a == b:
            return -1

        return len(a)
        