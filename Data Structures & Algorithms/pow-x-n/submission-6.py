class Solution:
    def myPow(self, x: float, n: int) -> float:
        ''' Recursion: O(logn) - Each step halves n
        power(2,5) → calls power(2,2)
        power(2,2) → calls power(2,1)
        power(2,1) → calls power(2,0)
        power(2,0) → returns 1 (base case)
        power(2,1) → returns 1*1*2 = 2
        power(2,2) → returns 2*2 = 4
        power(2,5) → returns 4*4*2 = 32
        '''
        def power(x, n):
            if n == 0:
                return 1
            # recursively call (x, n // 2) until n = 0
            half = power(x, n // 2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        # if n < 0: turn n positive then compute (1/x)^n
        if n < 0:
            x = 1/x
            n = -n
        
        return power(x, n)