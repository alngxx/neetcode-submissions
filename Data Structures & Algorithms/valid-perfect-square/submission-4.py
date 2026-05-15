class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Brute force
        if num == 0 or num == 1:
            return True
        i = 1
        while i*i <= num:
            i += 1
            if i*i == num:
                return True
        return False
        


        