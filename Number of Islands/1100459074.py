class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def search(x, y):
            if grid[x][y] == "0":
                return

            visited.add((x, y))

            if x + 1 < len(grid) and (x + 1, y) not in visited:
                search(x + 1, y)
            if x - 1 >= 0 and (x - 1, y) not in visited:
                search(x - 1, y)
            if y + 1 < len(grid[x]) and (x, y + 1) not in visited:
                search(x, y + 1)
            if y - 1 >= 0 and (x, y - 1) not in visited:
                search(x, y - 1) 

        visited = set()
        total = 0

        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry == "1" and (i, j) not in visited:
                    total += 1
                    search(i, j)
        
        return total






            
