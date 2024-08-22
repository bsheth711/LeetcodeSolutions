class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        backup = deepcopy(matrix)
        offset = len(backup) - 1

        for i, row in enumerate(backup):
            for j, num in enumerate(row):
                matrix[j][offset-i] = num

