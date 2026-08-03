class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check all rows
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        # 2. Check all cols
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        # 3. Check all 9 3x3 squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i     # (square // 3) * 3: starting row of current square
                    col = (square % 3) * 3 + j      # (square % 3) * 3: starting col of current square
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True