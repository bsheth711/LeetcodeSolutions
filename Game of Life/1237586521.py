class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        newBoard = [[0] * len(board[0]) for x in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                newBoard[i][j] = self.getValue(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = newBoard[i][j]


    def getValue(self, board, x, y):
        directions = [1, 0, -1]
        alive = 0

        isAlive = False
        if board[x][y] == 1:
            isAlive = True

        for i in directions:
            for j in directions:
                if i == 0 and j == 0:
                    continue
                
                val = self.tryToGet(board, x + i, y + j)
                if val == 1:
                    alive += 1
        
        if isAlive and alive < 2:
            return 0
        if isAlive and (alive == 2 or alive == 3):
            return 1
        if isAlive and alive > 3:
            return 0
        if not isAlive and alive == 3:
            return 1

        return board[x][y]
    
    def tryToGet(self, board, x, y):
        if x < 0 or y < 0:
            return 0
        
        if x >= len(board) or y >= len(board[x]):
            return 0

        return board[x][y]