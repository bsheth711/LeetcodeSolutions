class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0

        for i, c in enumerate(s):
            if i+1 < len(s) and mapping[c] < mapping[s[i+1]]:
                total -= mapping[c]
            else:
                total += mapping[c]

        return total
            
