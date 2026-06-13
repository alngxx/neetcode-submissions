class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """ DP Bottom-up: O(m*n)"""
        n = amount   
        dp = [99999] * (n + 1)          # dp[i] = min coins to make up amount i
        dp[0] = 0                       # base case: 0 coin to make up amount 0
        
        for i in range(1, n + 1):
            # try all kind of coin <= current amount i
            for coin in coins:
                if coin <= i:
                    # Take the min between:
                    # 1. not to take coin: C[i]
                    # 2. take coin: C[i - coin]
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[n] != 99999:
            return dp[n]
        else:
            return -1 