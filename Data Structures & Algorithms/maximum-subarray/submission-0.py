class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]

        for i in range (1, len(nums)):
            # Either extend the current subarray, or start a fresh one
            cur = max(cur + nums[i], nums[i])
            # Update max sum so far
            res = max(cur, res)
        return res
                