class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        j = num

        while i <= j:
            mid = (i+j) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                i = mid + 1
            else:
                j = mid - 1
        return False

        