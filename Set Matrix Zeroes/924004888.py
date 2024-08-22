class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        cols = set()

        for i, ls in enumerate(matrix):
            for j, num in enumerate(ls):
                if num == 0:
                    rows.add(i) 
                    cols.add(j)
        
        for i, ls in enumerate(matrix):
            for j, num in enumerate(ls):
                if i in rows:
                    matrix[i][j] = 0
                elif j in cols:
                    matrix[i][j] = 0
 

