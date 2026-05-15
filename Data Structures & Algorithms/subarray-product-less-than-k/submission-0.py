class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ Intuition: Sliding Window
        No. of valid subarray = Current window size
        """
        # Edge cases: k = 0 or 1 => None subarray < k
        if k <= 1:
            return 0

        l = 0
        count = 0
        product = 1

        for r in range(len(nums)):
            # Current window product as right pointer moves
            product *= nums[r]

            # While window invalid, shrink it from the left
            while product >= k:
                product //= nums[l]
                l += 1

            # No. of valid subarray = current window size
            count += r - l + 1
        return count
        