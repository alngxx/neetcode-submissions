class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ DP Bottom-up: O(m*n)
        - Try all possibilities and choose the min
        - C[j] = min ₍coinᵢ ≤ j₎ (1 + C[j - coinᵢ])
        <=> min_coins(i) = 1 + min_coins(i - coin)
        """
        n = amount
        C = [0] + [99999]*n   # C[i] = min number of coins to make amount i
        
        for i in range(1, n+1):
            # Try all type of coin <= amount i. Then take the best coin
            for coin in coins:
                if coin <= i:
                    # Take min between 2 cases:
                    # - C[i] = current known coins to make amount i
                    # - 1 (current coin) +  min coin to make amount (i - coin) i.e. C[i-coin]
                    C[i] = min(C[i], 1 + C[i - coin])
        
        if C[n] == 99999:    # If can't make up the amount
            return -1
        else:
            return C[n]