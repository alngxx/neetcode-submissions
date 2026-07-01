class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """ Grid Traversal: O(m * n), O(1)
        1. Scan every cell in the grid
        2. If cell is land, add 4 (all sides count as perimeter)
        3. For each neighbor (right and down only, avoid double counting) that is also land, 
        subtract 2 (shared edge is not perimeter)
        """
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += 4
                    # i + 1 < rows: make sure not out of bounds
                    # grid[i+1][j] == 1: below cell is land
                    if i + 1 < rows and grid[i+1][j] == 1:
                        res -= 2
                    if j + 1 < cols and grid[i][j+1] == 1:
                        res -= 2
        return res
                    

        