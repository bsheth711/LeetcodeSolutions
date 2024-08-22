class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        intBoard = self.makeIntBoard(board)

        #print(intBoard)

        if not self.checkSquares(intBoard):
            return False
        if not self.checkRows(intBoard):
            return False
        if not self.checkColumns(intBoard):
            return False
            
        return True
    
    def makeIntBoard(self, board):
        newBoard = []

        for row in board:
            newRow = []
            for element in row:
                if element == ".":
                    newRow.append(0)
                else:
                    newRow.append(int(element))
            
            newBoard.append(newRow)
        
        return newBoard
    
    def checkSquares(self, board):
        boardSize = 9
        for i in range(1, boardSize, 3):
            for j in range(1, boardSize, 3):
                hashtable = [0] * (boardSize+1)
                hashtable[board[i][j]] += 1
                hashtable[board[i][j+1]] += 1
                hashtable[board[i][j-1]] += 1
                hashtable[board[i+1][j]] += 1
                hashtable[board[i+1][j+1]] += 1
                hashtable[board[i+1][j-1]] += 1
                hashtable[board[i-1][j]] += 1
                hashtable[board[i-1][j+1]] += 1
                hashtable[board[i-1][j-1]] += 1

                for num in hashtable[1:]:
                    if num > 1:
                        return False
        
        return True


    
    def checkRows(self, board):
        boardSize = 9
        for row in board:
            hashtable = [0] * (boardSize+1)

            for element in row:
                hashtable[element] += 1
                if element != 0 and hashtable[element] > 1:
                    return False

        return True

    def checkColumns(self, board):
        boardSize = 9
        for i in range(boardSize):
            hashtable = [0] * (boardSize+1)
            for j in range(boardSize):
                hashtable[board[j][i]] += 1

                if board[j][i] != 0 and hashtable[board[j][i]] > 1:
                    return False

        return True



