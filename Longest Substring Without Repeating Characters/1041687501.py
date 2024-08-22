class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        charSet = set()
        cur = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[i])
            cur = max(cur, i - start + 1)
        
        return cur