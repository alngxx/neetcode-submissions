class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ DP Bottom-up: O(m*n)
        - Try all possibilities and choose the minimum
        - C[j] = min ₍coinᵢ ≤ j₎ (1 + C[j − coinᵢ])
        """
        n = amount   
        # DP array C[i] = min # of coins for amount i
        # Base case: C[0] = 0 => 0 coin to make 0
        C = [0] + [99999] * n  
        
        for i in range(1, n + 1):
            # Try all kind of coin <= current amount i
            for coin in coins:
                if coin <= i:
                    # Take the min between:
                    # C[i] = current known coins to make amount i
                    # 1 (current coin) + min coins to make (i-coin)
                    C[i] = min(C[i], 1 + C[i - coin])
        
        if C[n] == 99999:   
            return -1
        else:
            return C[n]