class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        Intuition:
        - Shift left and extracts LSB until exhausted, or n = 00...00
        - Summing up the LSB extracted one by one by shifting left those bits with the corresponding i
        '''

        res = 0
        for i in range(32):
            # Extract every bit (from LSB)
            bit = (n >> i) & 1

            # Summing up the value into integer
            # Example: 
            # i = 0: LSB shift lefts by 31 bits to become MSB
            # i = 1: Second LSB shift lefts by 30 bits to become second MSB
            res += bit << (31-i)

        return res
            
        