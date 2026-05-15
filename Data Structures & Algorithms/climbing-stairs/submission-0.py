class Solution:
    def climbStairs(self, n: int) -> int:
        """ DP Bottom-up: O(n)
        f(n) = # of ways to reach step n
        To reach step n, you only have 2 cases:
        - step (n-1) + 1 step
        - step (n-2) + 2 steps
        => f(n) = f(n-1) + f(n-2)
        """
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1] = 1     # 1 way to reach step 1
        dp[2] = 2     # 2 ways to reach step 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        