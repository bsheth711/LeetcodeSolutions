class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
   
        def dfs(board, cur, x, y): 
            nonlocal word
            nonlocal m
            nonlocal n

            if (x >= m
                or x < 0
                or y >= n
                or y < 0
                or len(cur) >= len(word)
                or board[x][y] != word[len(cur)]
                or (x, y) in cur):
                return False
            
            # step forward
            cur.add((x, y))

            if len(cur) == len(word):
                return True

            # recurse 
            up = dfs(board, cur, x - 1, y) 
            down = dfs(board, cur, x + 1, y)
            left = dfs(board, cur, x, y - 1)
            right = dfs(board, cur, x, y + 1)
            
            # step backward
            cur.remove((x, y))

            return up or down or left or right

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(board, set(), i, j):
                        return True
        
        return False
 
            
            