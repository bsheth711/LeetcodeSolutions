class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        processed = 0
        offset = 0

        while processed < total:

            for j in range(offset, n - offset):
                res.append(matrix[offset][j])

            processed += n - 2 * offset

            for i in range(offset + 1, m - offset):
                res.append(matrix[i][n - offset - 1])

            processed += m - 2 * offset - 1

            if processed == total:
                break
 
            for j in range(n - offset - 2, offset - 1, -1):
                res.append(matrix[m - offset - 1][j])
            
            processed += n - 2 * offset - 1
            
            for i in range(m - offset - 2, offset, -1):
                res.append(matrix[i][offset])
            
            processed += m - 2 * offset - 2
            
            offset += 1
        
        return res
        
            
        
        
                










        