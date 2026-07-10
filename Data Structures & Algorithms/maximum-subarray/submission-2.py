class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]

        for i in range(1, len(nums)):
            # either extend the current subarray, or start a fresh one
            cur = max(cur + nums[i], nums[i])

            # update max_sum
            res = max(res, cur)
        
        return res
                