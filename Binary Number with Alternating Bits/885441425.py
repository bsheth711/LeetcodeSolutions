class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = self.toBinary(n)
        prev = 3

        for digit in binary:
            if prev == digit:
                return False
            prev = digit

        return True

    def toBinary(self, n: int) -> list[int]:
        ls = []

        while n > 0:
            ls.append(n % 2)
            n //= 2

        return ls
