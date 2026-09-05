class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """ Iterative Simulation: O(m * n) """
        res = []
        top, bot = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bot:
            for i in range(left, right + 1):        # 1, 2, 3
                res.append(matrix[top][i])      
            top += 1

            for i in range(top, bot + 1):           # 6, 9
                res.append(matrix[i][right])    
            right -= 1

            # ensure there still row/col after two shrinks
            if not (left <= right and top <= bot):
                break
                
            for i in range(right, left - 1, -1):    # 8, 7
                res.append(matrix[bot][i])
            bot -= 1
            
            for i in range(bot, top - 1, -1):       # 4
                res.append(matrix[i][left])
            left += 1

        return res