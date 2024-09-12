class Solution:
    def numDecodings(self, s: str) -> int:
        doubleDigits = {str(x) for x in range(10, 27)}
        oldest = 1
        if s[0] == '0':
            return 0
        else:
            older = 1

        res = older
        
        for i in range(2, len(s) + 1):
            first = s[i - 1: i]
            second = s[i - 2: i]
            res = 0

            if first != "0":
                res += older
            if second in doubleDigits:
                res += oldest
            
            oldest = older
            older = res

        return res