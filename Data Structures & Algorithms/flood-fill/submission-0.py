class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """ DFS: O(m * n), O(m * n)
        1. Save origin color of given pixel
        2. If origin color == new color, return image
        3. Define DFS(r, c) where r, c are coordinates of current pixel
        4. If current pixle out of bounds, or != origin color, return (stop this branch)
        5. Else, paint it with new color, and DFS all its 4 neighbors
        """
        # edge case: original color = new color, no change needed
        origin = image[sr][sc]
        if origin == color:
            return image
        
        m, n = len(image), len(image[0])
        def dfs(r, c):
            # if current pixel out of bounds, or != origin, stop flooding this branch
            if (r < 0) or (c < 0) or (r > m - 1) or (c > n - 1) or image[r][c] != origin:
                return 
            
            # paint this pixel, then flood all its 4 neighbors
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image