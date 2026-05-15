class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []

        for i in range(len(matrix[0])):     # Loop over columns
            temp = []

            for j in range(len(matrix)):    # Loop over rows
                temp.append(matrix[j][i])   # Take element at row j, column i

            res.append(temp)                # Add rows to new matrix

        return res