
startFrom = 0

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        global startFrom
        startFrom = 0

        return self.helper(s, t)
   
    def helper(self, s, t):
        global startFrom

        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False

        prev = self.isSubsequence(s[:-1], t)

        if not prev:
            return False 
        
        for i in range(startFrom, len(t)):
            if t[i] == s[-1]:
                startFrom = i + 1
                return True

        return False
        
 