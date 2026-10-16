class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        """ Fixed-size Sliding Window: O(n), O(1) """
        nums.sort()
        res = nums[k - 1] - nums[0]

        for i in range(k, len(nums)):
            diff = nums[i] - nums[i - k + 1]
            res = min(res, diff)
         
        return res