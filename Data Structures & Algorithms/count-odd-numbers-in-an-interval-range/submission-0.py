class Solution:
    def countOdds(self, low: int, high: int) -> int:
        def odd(num):
            return num % 2 == 1

        if odd(low) and odd(high):
            return (high-low) // 2 + 1
        
        elif odd(low) or odd(high):
            return (high-low-1) // 2 + 1
        
        else:
            return (high-low) // 2 
        