class Solution:
    def isHappy(self, n: int) -> bool:
        cur = n

        for i in range(100):
            digits = self.getDigits(cur)
            cur = self.getNumber(digits) 
            if cur == 1:
                return True
        
        return False
    
    def getNumber(self, digits): 
        total = 0

        for digit in digits:
            digit *= digit
            total += digit
        
        return total

    def getDigits(self, n):
        if n == 0:
            return [0]

        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        return digits 