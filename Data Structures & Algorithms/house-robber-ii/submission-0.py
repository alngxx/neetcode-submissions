class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge case
        if n == 1:
            return nums[0]
        
        # Take max of two cases:
        # 1. Exclude first house: Rob house 1 → n-1
        # 2. Exclude last house: Rob house 0 → n-2
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:-1]))  # rob_1 is method of class → call it using self.
    
    def rob_1(self, nums: List[int]) -> int:     # Same as House Robber I
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0] * n                    # dp[i] = max money can rob up to house i
        dp[0] = nums[0]                 # dp[0] = money at first house 0
        dp[1] = max(nums[0], nums[1])   # dp[1] = greater money at house 0 or 1

        # Bottom-up: dp[2] → dp[n-1]
        for i in range(2, n):
            # When come to house i, only two choices:
            # 1. Don't rob: dp[i] = dp[i-1]
            # 2. Rob: Thus can't rob house i-1. Max money = money at house i + max money rob up to house [i-2]
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]