class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        cur = 0
        mask = 1

        for i in range(31, -1, -1):
            leftBit = (left >> i) & mask
            rightBit = (right >> i) & mask

            if rightBit == 1:
                if leftBit == 1:
                    cur += 1
                else: 
                    for j in range(i + 1):
                        cur <<= 1
                    break
                     
            cur <<= 1
        
        cur >>= 1

        return cur


