class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1 

        return self.fix(digits, len(digits) - 1)

    def fix(self, digits, place):
        if digits[place] > 9:
            digits[place] -= 10

            if place != 0:
                digits[place - 1] += 1
            else:
                digits.insert(0, 1)
                return digits

            self.fix(digits, place-1)

        return digits
