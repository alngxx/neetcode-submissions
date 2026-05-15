class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        Recursion: O(logn) - Each step halves n
        power(2,10) → calls power(2,5)
        power(2,5) → calls power(2,2)
        power(2,2) → calls power(2,1)
        power(2,1) → calls power(2,0)
        power(2,0) → returns 1 (base case)
        power(2,1) → returns 1*1*2 = 2
        power(2,2) → returns 2*2 = 4
        power(2,5) → returns 4*4*2 = 32
        power(2,10) → returns 32*32 = 1024
        '''

        def power(x,n):
            # Base case
            if n == 0:
                return 1
            
            half = power(x, n//2)

            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
            
        if n < 0:
            x = 1/x
            n = -n
        
        return power(x,n)

        
        