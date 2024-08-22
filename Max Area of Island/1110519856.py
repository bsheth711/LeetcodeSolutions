class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        visited = set()

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1 and (i, j) not in visited:
                    best = max(best, self.bfs(grid, visited, i, j))
        
        return best

        
    def bfs(self, grid, visited, i, j):
        q = []
        q.append((i, j))

        m = len(grid)
        n = len(grid[0])
        counter = 0

        print(q)
        while q:
            toAdd = []

            for _ in range(len(q)):
                cur = q.pop()
                x = cur[0]
                y = cur[1]

                if cur not in visited:
                    counter += 1

                    if y + 1 < n and grid[x][y+1] == 1: 
                        toAdd.append((x, y+1))
                    if y - 1 >= 0 and grid[x][y-1] == 1:
                        toAdd.append((x, y-1))
                    if x + 1 < m and grid[x+1][y] == 1:
                        toAdd.append((x+1, y))
                    if x - 1 >= 0 and grid[x-1][y] == 1:
                        toAdd.append((x-1, y))

                    visited.add(cur)
                
            q.extend(toAdd)
        
        return counter



