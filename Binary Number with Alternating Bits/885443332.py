class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 3

        while n > 0:
            digit = n % 2
            if digit == prev:
                return False
            n //= 2
            prev = digit

        return True