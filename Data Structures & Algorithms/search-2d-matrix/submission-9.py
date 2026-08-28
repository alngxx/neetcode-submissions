class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ Binary Search: O(log(m) + log(n)) = O(log(m * n))
        Perform Binary Search twice:
        1. First Binary Search to find target's row
        2. Second Binary Search to find target in that row
        """
        # 1. Find target's row
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break       # now, row = target's row

        # 2. Find target in that row
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False