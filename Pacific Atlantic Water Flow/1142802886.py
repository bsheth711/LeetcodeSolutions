class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        numRows = len(heights)
        numCols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(x, y, visited, prevHeight):
            if (
                (x, y) in visited
                or x < 0
                or y < 0
                or x >= numRows
                or y >= numCols
                or heights[x][y] < prevHeight
            ):
                return

            visited.add((x, y))
            dfs(x + 1, y, visited, heights[x][y])
            dfs(x, y + 1, visited, heights[x][y])
            dfs(x - 1, y, visited, heights[x][y])
            dfs(x, y - 1, visited, heights[x][y])

        for x in range(numRows):
            dfs(x, 0, pacific, heights[x][0])
            dfs(x, numCols - 1, atlantic, heights[x][numCols - 1])
        
        for y in range(numCols):
            dfs(0, y, pacific, heights[0][y])
            dfs(numRows - 1, y, atlantic, heights[numRows - 1][y])
        
        res = []
        for x in range(numRows):
            for y in range(numCols):
                if (x, y) in pacific and (x, y) in atlantic:
                    res.append([x, y])
        
        return res

        