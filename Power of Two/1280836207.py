class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # if there is a single 1 in the binary representation it is a power of two

        hasOne = False

        while n:
            if n & 1 == 1:
                if hasOne:
                    return False
                hasOne = True
            n >>= 1
        
        return True
