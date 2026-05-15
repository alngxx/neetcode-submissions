class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
    
        res = x
        if n > 0:
            for i in range(1, n):
                res *= x
            return res
        
        elif n < 0:
            for i in range(1, -n):
                res *= x
            return 1/res
        