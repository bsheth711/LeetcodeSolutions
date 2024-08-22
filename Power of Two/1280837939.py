class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # if there is a single 1 in the binary representation it is a power of two

        counter = 0

        while n:
            if n & 1 == 1:
                counter += 1
            n >>= 1
        
        return counter == 1
