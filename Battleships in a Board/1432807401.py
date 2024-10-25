class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        m = len(board)
        n = len(board[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i, j) not in visited:
                    count += 1
                    self.dfs(board, i, j, m, n, visited)
        
        return count

    def dfs(self, board, x, y, m, n, visited):
        if (x >= m
            or x < 0
            or y >= n
            or y < 0
            or board[x][y] != 'X'
            or (x, y) in visited):
            return
        
        visited.add((x, y))

        self.dfs(board, x + 1, y, m, n, visited)
        self.dfs(board, x - 1, y, m, n, visited)
        self.dfs(board, x, y + 1, m, n, visited)
        self.dfs(board, x, y - 1, m, n, visited)
        