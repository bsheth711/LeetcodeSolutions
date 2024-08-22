class Solution: 
    def numDecodings(self, s: str) -> int:   
        if not s:
            return 1

        digits = []
        for c in s:
            digits.append(int(c))
        
        last2 = 1
        last = 1
        if digits[0] == 0:
            last = 0
        
        res = last

        for i in range(1, len(digits)):
            res = 0
            single = digits[i]
            double = digits[i] + digits[i - 1] * 10

            if single != 0:
                res += last
            if double > 9 and double <= 26:
                res += last2
            last2 = last
            last = res
             
        return res



