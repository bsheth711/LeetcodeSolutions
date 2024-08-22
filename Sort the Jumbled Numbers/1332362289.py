class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]: 
        return sorted(nums, key=lambda x: self.realValue(mapping, x))
        
    def realValue(self, mapping, num):
        realDigits = []

        if num == 0:
            realDigits = [mapping[0]]

        while num > 0:
            digit = num % 10
            realDigits.append(mapping[digit])
            num //= 10
        
        real = 0
        for digit in reversed(realDigits):
            real *= 10
            real += digit

        print(real)
        
        return real
            
