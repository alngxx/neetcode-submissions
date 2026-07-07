class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ 1D DP: O(n²), O(n²)
        1. Start with row 0 = [1]
        2. For each new row, pad the previous row with a 0 on each side
        e.g. prev = [1,2,1] -> temp = [0,1,2,1,0]
        3. Each new value = sum of two adjacent numbers in temp
        (this trick avoids checking edge cases for first/last element)
        4. Repeat until numRows rows are built
        """
        res = [[1]]

        for i in range(numRows - 1):
            row = []
            temp = [0] + res[-1] + [0]

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])

            res.append(row)
        return res        