'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        cur = set()
   
        def dfs(i, x, y): 

            if (x >= m
                or x < 0
                or y >= n
                or y < 0
                or i >= len(word)
                or board[x][y] != word[i]
                or (x, y) in cur):
                return False
            
            # step forward
            cur.add((x, y))

            i += 1
            if i == len(word):
                return True

            # recurse 
            up = dfs(i, x - 1, y) 
            down = dfs(i, x + 1, y)
            left = dfs(i, x, y - 1)
            right = dfs(i, x, y + 1)
            
            # step backward
            cur.remove((x, y))

            return up or down or left or right

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        
        return False
''' 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r, c) in path
            ):
                return False
            path.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            path.remove((r, c))
            return res

        '''
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        '''
            
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False