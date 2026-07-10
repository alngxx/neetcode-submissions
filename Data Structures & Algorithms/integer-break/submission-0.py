class Solution:
    def integerBreak(self, n: int) -> int:
        """ 1D DP: O(n²), O(n)
        1. dp[i] = "max product" breaking i 
        2. For each i, try every j (1 <= j < i):
            a) leave unsplit -> j * (i - j)
            b) split further -> j * dp[i - j]
        3. Must compare both (a) and (b): dp[i-j] is NOT always >= (i - j)
        4. Return dp[n]
        """
        dp = [1] * (n + 1)

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
        
        return dp[n]