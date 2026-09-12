class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # stop if out of bounds or not 'O' (already 'safe' or 'X')
            if (r < 0) or (c < 0) or (r > rows - 1) or (c > cols - 1) or board[r][c] != 'O':
                return
            
            # otherwise, mark as 'safe' only if connected to a border 'O' (flood fill below)
            board[r][c] = 'safe'
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
        
        # flood fill from a border 'O' to all connected cells, mark as 'safe'
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                # if mark as 'safe', they are non-surrounded regions, flip back to 'O'
                if board[r][c] == 'safe':
                    board[r][c] = 'O'
                # otherwise, they are surrounded regions, change to 'X'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'