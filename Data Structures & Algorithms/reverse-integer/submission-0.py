class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        
        # Remove sign for easier reversing
        x = abs(x)
        res = 0

        while x:
            mod = x % 10   # Get last digit
            x //= 10        # Remove last digit
            
            # Build up reverse int
            res = res*10 + mod
            # Ensure do not exceed 32-bit range
            if res > 2**31 - 1:
                return 0
                
        return sign*res
        