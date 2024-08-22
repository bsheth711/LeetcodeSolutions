class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_MAX = len(board)
        COL_MAX = len(board[0])
        cur = set()

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(ROW_MAX):
            for j in range(COL_MAX):
                if self.dfs(0, i, j, board, word, cur):
                    return True
        
        return False
    
    def dfs(self, i, x, y, board, word, cur):
            if i == len(word):
                return True

            if (x >= len(board)
                or x < 0
                or y >= len(board[0])
                or y < 0
                or board[x][y] != word[i]
                or (x, y) in cur):
                return False
            
            # step forward
            cur.add((x, y))

            # recurse 
            up = self.dfs(i + 1, x - 1, y, board, word, cur) 
            down = self.dfs(i + 1, x + 1, y, board, word, cur)
            left = self.dfs(i + 1, x, y - 1, board, word, cur)
            right = self.dfs(i + 1, x, y + 1, board, word, cur)
            
            # step backward
            cur.remove((x, y))

            return up or down or left or right