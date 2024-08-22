class Solution:
    def myPow(self, x: float, n: int) -> float:
        absN = abs(n)

        if x == 0:
            return 0
        if absN == 0:
            return 1

        res = self.myPow(x * x, absN // 2)
        if absN % 2:
            res *= x

        if n < 0:
            return 1 / res
            
        return res
