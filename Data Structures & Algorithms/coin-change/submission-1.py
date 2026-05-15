class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount
        C = [0] + [99999] * n

        for i in range(1, n+1):
            for coin in coins:
                if coin <= i:
                    C[i] = min(C[i], 1 + C[i - coin])
        
        return -1 if C[n] == 99999 else C[n]
        