class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ DFS: O(m * n), O(m * n)
        For every cell, run DFS and update max_area
        dfs(r, c):
        1. Return 0 if out of bounds, water (0) (stop this branch)
        2. Mark the cell as visited: grid[r][c] = 0
        3. Return 1 + area from all 4 neighbors
        """
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if (r < 0) or (c < 0) or (r > rows - 1) or (c > cols - 1) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0     
            return 1 + (dfs(r - 1, c) +
                        dfs(r + 1, c) + 
                        dfs(r, c - 1) + 
                        dfs(r, c + 1))

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r, c))
        
        return max_area