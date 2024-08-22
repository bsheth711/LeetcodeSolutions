class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        offsets = [1, -1]
        visited = set()
        possible = set()
        minutes = -1
        q = []

        '''
        2 1 1
        1 1 1
        0 1 2
        '''
        
        # find the greatest distance between a rotten orange and a fresh orange
        # if not all oranges can spoil, instead return -1

        # ok that didn't work, lets try brute force

        def isValid(i, j, grid):
            if (i, j) in visited:
                return False
            if i < 0 or i >= m:
                return False
            if j < 0 or j >= n:
                return False
            if grid[i][j] != 1:
                return False
            
            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    possible.add((i, j))
        
        if not possible:
            return 0

        while q:
            toExtend = []
            for _ in range(len(q)):
                (i, j) = q.pop()
                
                for x in offsets:
                    if isValid(i + x, j, grid):
                        toExtend.append((i + x, j))
                        visited.add((i + x, j))

                for y in offsets:
                    if isValid(i, j + y, grid):
                        toExtend.append((i, j + y))
                        visited.add((i, j + y))
            
            q.extend(toExtend) 
            minutes += 1
                

        for orange in possible:
            if orange not in visited:
                return -1
        
        return minutes
    