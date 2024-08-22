# this is like the fibonacci sequence
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        num1 = 1
        num2 = 2
        s = num1 + num2
        
        for i in range(n-3):
            tmp = num1
            num1 = num2
            num2 = tmp + num2
            s = num1 + num2

        return s