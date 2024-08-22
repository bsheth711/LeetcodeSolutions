class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [ [0] * n for i in range(n) ]

        cur = 1
        top = 0
        right = n - 1
        bottom = n - 1
        left = 0
        n2 = n * n

        while cur <= n2:
            # top
            for j in range(left, right + 1):
                matrix[top][j] = cur
                cur += 1
            top += 1

            # right
            for i in range(top, bottom + 1):
                matrix[i][right] = cur
                cur += 1
            right -= 1

            # bottom
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = cur
                cur += 1
            bottom -= 1

            # left
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = cur
                cur += 1
            left += 1
        
        return matrix