class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def search(i, x, y, visited):
            if (x, y) in visited:
                return False
            if x >= m or x < 0:
                return False
            if y >= n or y < 0:
                return False
            if board[x][y] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            
            visited.add((x, y))

            up = search(i + 1, x + 1, y, visited)
            down = search(i + 1, x - 1, y, visited)
            right = search(i + 1, x, y + 1, visited)
            left = search(i + 1, x, y - 1, visited)

            visited.remove((x, y))

            return up or down or left or right
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    if search(0, x, y, set()):
                        return True
        
        return False