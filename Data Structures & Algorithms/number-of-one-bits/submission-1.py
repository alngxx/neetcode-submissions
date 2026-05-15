class Solution:
    def hammingWeight(self, n: int) -> int:
        ''' 
        Example: n = 11 
        i = 0: (n >> 0) = 1011 → last bit = 1 → res = 1
        i = 1: (n >> 1) = 0101 → last bit = 1 → res = 2
        i = 2: (n >> 2) = 0010 → last bit = 0 → res = 2
        i = 3: (n >> 3) = 0001 → last bit = 1 → res = 3
        i = 4: (n >> 4) = 0000 -> not if (n >> 4)
        '''

        res = 0  
        # Iterate over all 32 bits of the integer
        for i in range(32):
            # Right shift n by i bits, then check the least significant bit
            # (n >> i) shifts the binary representation to the right
            # & 1 extracts the last bit (0 or 1): 1 = 00...001
            if (n >> i) & 1:
                # If the bit is 1, increment the counter
                res += 1  

        return res
        
        