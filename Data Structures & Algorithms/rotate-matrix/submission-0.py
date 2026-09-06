class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """ Transpose + Reverse: O(n²)
        Rotate matrix 90 degrees is simply two in-place operations:
        1. Transpose - swap rows & cols: [[1,4,7], [2,5,8], [3,6,9]]
        2. Reverse - each row:           [[7,4,1], [8,5,2], [9,6,3]]
        """
        n = len(matrix)

        # 1. Tranpose: swap along diagonal - execept diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Reverse each row
        for row in matrix:
            row.reverse()

        # For 4x4 matrix, the transpose belike:
        # swap [1, 9, 11] and [2, 13, 15]
        # swap [8, 10] and [3, 14]
        # swap [7, 12]
        # we never swap the diagonal, as the inner loop is (i + 1, n)