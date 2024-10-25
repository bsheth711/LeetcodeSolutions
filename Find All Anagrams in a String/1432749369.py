class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        counts = [0] * 26
        window = [0] * 26
        offset = 97
        ret = []
        loc = 0

        for c in p:
            counts[ord(c) - offset] += 1

        for i in range(len(p)):
            window[ord(s[i]) - offset] += 1
        
        if counts == window:
            ret.append(loc)
 
        for i in range(len(p), len(s)):
            window[ord(s[loc]) - offset] -= 1
            window[ord(s[i]) - offset] += 1

            loc += 1

            if window == counts:
                ret.append(loc)
        
        return ret

        









        