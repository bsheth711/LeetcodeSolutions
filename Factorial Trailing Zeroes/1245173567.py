class Solution:
    def trailingZeroes(self, n: int) -> int:
        # there is probably some math trick because (10^4)! would take forever to compute 
        num2 = 0
        num5 = 0

        while n > 0:
            num2 += self.extract(n, 2)
            num5 += self.extract(n, 5)
            n -= 1
        
        return min(num2, num5)

    def extract(self, a, b):
        counter = 0

        while a % b == 0:
            a //= b
            counter += 1
             
        return counter
