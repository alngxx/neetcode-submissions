class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """ 2D DP Bottom-up: O(m * n), O(m * n)
        1. dp[i][j] = unique paths from [0][0] to [i][j]
        2. Any cell (r, c) can only be reached from above (r - 1, c) or from left (r, c - 1)
        3. Base cases:
        - Row 0 has only 1 way (move purely Right)
        - Column 0 has only 1 way (move purely Down)
        """
        dp = [[1] * n for _ in range(m)]

        # dp[0][c] and dp[r][0] only has 1 path through
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
                
        return dp[-1][-1] 
        