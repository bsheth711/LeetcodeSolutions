class Solution:
    def isHappy(self, n: int) -> bool:
        cur = n

        for i in range(100):
            cur = self.getNew(cur)
            if cur == 1:
                return True
        
        return False
    
    def getNew(self, n):
        total = 0

        while n > 0:
            total += (n % 10) ** 2
            n //= 10

        return total