class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # gradeschool multiplication
        cur = 0
        offset = 1
        '''
        40
        25
        '''

        for c1 in reversed(num1):
            place = 1
            for c2 in reversed(num2):
                cur += int(c1) * int(c2) * offset * place

                place *= 10
            
            offset *= 10
        
        return str(cur)


        