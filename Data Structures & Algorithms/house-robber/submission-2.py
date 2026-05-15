class Solution:
    def rob(self, nums: List[int]) -> int:
        """ DP Bottom-up: dp[i] = max money can rob up to house i
        When come to house i, you pick the best of two choices:
        1. Skip house i: Thus dp[i] = dp[i-1]
        2. Rob house i:
        - So you can't rob house i-1
        - Thus, add money at house i (= nums[i]) + max money can rob up to house (i-2)
        => dp[i] = nums[i] + dp[i-2]
        """
        n = len(nums)                   # No. of house: 0 → n-1
        if n <= 1:
            return nums[0]

        dp = [0] * n                    # dp[i] = max money can rob up to house i
        # Base case
        dp[0] = nums[0]                 # dp[0] = money of house 0
        dp[1] = max(nums[0], nums[1])   # dp[1] = greater money of house 0 & 1

        # Bottom-up: Calculate from dp[2] → dp[n-1]
        for i in range(2, n):
            dp[i] = max (dp[i - 1], 
                        nums[i] + dp[i - 2])

        return dp[-1]