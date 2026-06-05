class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ Binary Search: O(log(m) + log(n)) = O(log(m * n))
        Perform Binary Search twice:
        1. First Binary Search to find target's row
        2. Second Binary Search to find target in that row
        """

        # 1. Find target's row
        top = 0                     # first row
        bot = len(matrix) - 1       # last row
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            # break if both conditions above not satisfy
            # matrix[row][0] <= target <= matrix[row][-1] 
            else:
                break       # now, target is inside matrix[row]

        # 2. Find target inside matrix[row]
        row = (top + bot) // 2
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target >= matrix[row][mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return False