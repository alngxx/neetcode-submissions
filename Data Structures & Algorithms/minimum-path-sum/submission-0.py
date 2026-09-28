class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        """ 2D Bottom-up: O(m * n), O(m * n)
        1. dp[r][c] = min path sum from (r,c) to bottom right
        2. From (r,c) you can only go down or right, so:
        dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
        3. Return dp[0][0]
        """
        m, n = len(grid), len(grid[0])

        # dp[r][c] = min path sum from grid[r][c] to grid[m - 1][n - 1]
        dp = [[float('inf')] * (n) for _ in range(m)]    

        # fill from [m-1][n-1] to [0][0]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # base case
                if r == m - 1 and c == n - 1:
                    dp[r][c] = grid[r][c]
                # bottom row, so only comes from right cell
                elif r == m - 1:
                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                # right col, so only comes from down cell
                elif c == n - 1:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])
        
        return dp[0][0]