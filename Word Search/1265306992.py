class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_MAX = len(board)
        COL_MAX = len(board[0])
        WORD_LEN = len(word)
        cur = set()
   
        def dfs(i, x, y): 
            if i == WORD_LEN:
                return True

            if (x >= ROW_MAX
                or x < 0
                or y >= COL_MAX
                or y < 0
                or board[x][y] != word[i]
                or (x, y) in cur):
                return False
            
            # step forward
            cur.add((x, y))

            # recurse 
            up = dfs(i + 1, x - 1, y) 
            down = dfs(i + 1, x + 1, y)
            left = dfs(i + 1, x, y - 1)
            right = dfs(i + 1, x, y + 1)
            
            # step backward
            cur.remove((x, y))

            return up or down or left or right

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(ROW_MAX):
            for j in range(COL_MAX):
                if dfs(0, i, j):
                    return True
        
        return False