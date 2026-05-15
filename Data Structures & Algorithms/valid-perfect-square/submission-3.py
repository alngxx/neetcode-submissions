class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = num
        if n == 0 or n == 1:
            return True
        i = 1
        while i*i <= n:
            i += 1
            if i*i == n:
                return True
        return False


        