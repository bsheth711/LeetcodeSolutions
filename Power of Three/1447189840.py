import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        

        num = math.log(n, 3)

        return math.isclose(num, round(num), rel_tol=1e-11)
        