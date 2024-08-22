class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        totals = triangle[-1][:]

        for i in range(-2, -(len(triangle) + 1), -1):
            for j in range(len(triangle[i])):
                totals[j] = min(totals[j], totals[j + 1]) + triangle[i][j]
        
        return totals[0]


        