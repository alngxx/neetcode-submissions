class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ 1D DP: O(n²), O(n)
        1. dp[i] = length of LIS starting at index i
        2. For i in (n-1...0), check every j > i
        - If nums[i] < nums[j]: dp[i] = max(dp[i], 1 + dp[j])
        - We can extend the subsequence starting at j i.e. dp[j]
        - Add 1 for current nums[i]
        3. Return max(dp)
        """
        n = len(nums)
        # dp[i] = LIS starting at i
        # each element is a subsequence length 1
        dp = [1] * n        

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp) 
        