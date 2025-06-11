class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            rowNumbers = {"1","2","3","4","5","6","7","8","9"}
            colNumbers = {"1","2","3","4","5","6","7","8","9"}
            boxNumbers = {"1","2","3","4","5","6","7","8","9"}
            for j in range(9):
                if board[i][j] in rowNumbers: #board[i][j] != ".":
                    rowNumbers.discard(board[i][j])
                    # print(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False

                if board[j][i] in colNumbers: #board[i][j] != ".":
                    colNumbers.discard(board[j][i])
                elif board[j][i] == ".":
                    pass
                else:
                    return False
        
        for i in range(3):
            for j in range(3):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(3):
            for j in range(3,6):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(3):
            for j in range(6,9):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(3,6):
            for j in range(3):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(6,9):
            for j in range(3):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:
                    return False
        boxNumbers = {"1","2","3","4","5","6","7","8","9"}
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] in boxNumbers: #board[i][j] != ".":
                    boxNumbers.discard(board[i][j])
                elif board[i][j] == ".":
                    pass
                else:   
                    return False
        return True

# Or

class Solution:
    def isValidSudoku(self, board):
        # Checking Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
        # Checking Columns
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
        # Checking Boxes
        starts = [(0, 0), (0, 3), (0, 6),
                (3, 0), (3, 3), (3, 6),
                (6, 0), (6, 3), (6, 6)]
        for i,j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
        return True
        