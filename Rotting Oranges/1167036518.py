class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # do BFS solution
        q = []
        m = len(grid)
        n = len(grid[0])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        fresh = set()
        time = -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))
        
        if not fresh:
            return 0

        while q:
            toAdd = []
            time += 1
            print(q)

            for _ in range(len(q)):
                cur = q.pop()
                fresh.discard(cur)

                for x, y in offsets:
                    i = cur[0] + x
                    j = cur[1] + y

                    if i >= m or i < 0:
                        continue
                    if j >= n or j < 0:
                        continue
                    if grid[i][j] != 1:
                        continue
                    if (i, j) in visited:
                        continue
                    
                    toAdd.append((i, j))
                    visited.add((i, j))
            
            q.extend(toAdd)
        
        if fresh:
            return -1
        
        return time

                    




                
