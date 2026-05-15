class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1

        a = 0  # T(0) = 0
        b = 1  # T(1) = 1
        c = 1  # T(2) = 1

        # Compute T(i) = T(i-3) + T(i-2) + T(i-1) for i = 3 to n
        for _ in range(3, n+1):
            a, b, c = b, c, a + b + c   
        
        # At last, c = T(n)
        return c
        