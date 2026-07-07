class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """ 1D DP: O(n²), O(n²)
        1. Start with row 0: res = [[1]]
        2. For new row, pad the last row with a 0 on each side
        e.g. prev = [1,2,1] -> temp = [0,1,2,1,0]
        3. Each new value = sum of two adjacent numbers in temp
        4. Append new row to res
        5. Return res[-1]
        """
        res = [[1]]

        for i in range(rowIndex):
            row = []
            temp = [0] + res[-1] + [0]

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            
            res.append(row)
        
        return res[-1]