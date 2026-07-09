class Solution:
    def climbStairs(self, n: int) -> int:
        """ DP Bottom-up: O(n)
        To reach step n, you should come from 2 cases:
        - step (n-1) + 1 step
        - step (n-2) + 2 steps
        """
        if n <= 2:
            return n

        dp = [0] * (n+1)    # dp[i] = # ways to reach step i
        dp[1] = 1           # 1 way to reach step 1
        dp[2] = 2           # 2 ways to reach step 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]