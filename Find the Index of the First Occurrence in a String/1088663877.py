class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def isMatch(i, haystack, needle):
            for c in needle:
                if i >= len(haystack):
                    return False
                
                if c != haystack[i]:
                    return False
    
                i += 1
            
            return True

        for i in range(len(haystack)):
            if isMatch(i, haystack, needle):
                return i

        return -1


               
                