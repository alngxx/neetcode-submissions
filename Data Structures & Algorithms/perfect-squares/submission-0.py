class Solution:
    def numSquares(self, n: int) -> int:
        """ 1D DP: O(n * √n), O(n)
        1. dp[i] = min squares summing to i
        2. dp[0] = 0, dp[1] = 1
        3. For i in 2..n, try every square j * j <= i: 
            dp[i] = min(dp[i], dp[i - j*j] + 1)
        4. Return dp[n]
        """
        dp = [float('inf')] * (n + 1)      # init dp[i] = infinity so min(...) works
        dp[0] = 0                          
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        
        return dp[n]