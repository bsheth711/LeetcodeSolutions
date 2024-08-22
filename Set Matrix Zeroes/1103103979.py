class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if num == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
        
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        