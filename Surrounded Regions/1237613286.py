class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # heuristic: to not be surrounded on 4 edges, a group of O's must be touching the edge of 2D array
        # algo: go around edge and when O is found dfs and add to no flip list. Flip all Os not in no flip list

        m = len(board)
        n = len(board[0])
        visited = set()

        # upper edge
        for j in range(n):
            if board[0][j] ==  "O":
                self.dfs(board, visited, 0, j)

        # left edge
        for i in range(m):
            if board[i][0] ==  "O":
                self.dfs(board, visited, i, 0)

        # right edge
        for i in range(m):
            if board[i][n-1] ==  "O":
                self.dfs(board, visited, i, n-1)

        # bottom edge
        for j in range(n):
            if board[m-1][j] ==  "O":
                self.dfs(board, visited, m-1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
    
    def dfs(self, board, visited, x, y):
        if (x < 0 
            or x >= len(board)
            or y < 0
            or y >= len(board[0])
            or (x, y) in visited
            or board[x][y] != "O"):
            return
        
        visited.add((x, y))

        directions = [1, -1]

        for j in directions:
            self.dfs(board, visited, x, y + j)
        
        for i in directions:
            self.dfs(board, visited, x + i, y)

        '''
        0, 1
        0, -1
        1, 0
        -1, 0
        '''