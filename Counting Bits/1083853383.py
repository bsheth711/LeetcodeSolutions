class Solution:
    def countBits(self, n: int) -> List[int]:
         
        def hammingWeight(n: int) -> int:
            res = 0
        
            while n != 0:
                if (n - 1) % 2 == 0:
                    res += 1
                
                n = n >> 1
            
            return res


        res = []

        for i in range(n+1):
            res.append(hammingWeight(i))
        
        return res