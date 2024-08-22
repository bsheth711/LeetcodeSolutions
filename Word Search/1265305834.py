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

        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        
        return False