class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ 1D DP: O(n)
        1. dp[i] = max sum of subarray ending EXACTLY at i
        2. At every i, either dp[i]:
        - dp[i - 1] + nums[i]: continue current subarray
        - nums[i]: start a fresh one
        3. Return max(dp), not dp[-1] since max subarray may not ending at the end
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)      