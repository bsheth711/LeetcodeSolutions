class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if there is a single 1 in the binary representation it is a power of two

        return n and not (n & n - 1)
