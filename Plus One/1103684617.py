class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = -1

        digits[cur] += 1

        while digits[cur] > 9 and abs(cur-1) <= len(digits):
            digits[cur] = 0
            cur -= 1
            digits[cur] += 1
        
        if digits[0] > 9:
            digits[0] = 0
            digits.insert(0, 1)
        
        return digits