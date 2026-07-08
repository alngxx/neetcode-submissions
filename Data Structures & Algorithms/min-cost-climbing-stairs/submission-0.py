class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """ DP Bottom-Up: 
        dp[i] = min cost to reach step i
        To reach step i, we can either:
        1. Come from step i-1, after spending dp[i-1], then pay cost[i-1]
        2. Come from step i-2, after spending dp[i-2], then pay cost[i-1]
        """
        n = len(cost)
        dp = [0] * (n + 1)      # dp[i] = min cost to reach step i
        dp[0] = dp[1] = 0       # can start at either step 0 or 1 for free

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[n]


        