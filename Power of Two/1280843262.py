class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # if there is a single 1 in the binary representation it is a power of two

        return not (n & n - 1)
