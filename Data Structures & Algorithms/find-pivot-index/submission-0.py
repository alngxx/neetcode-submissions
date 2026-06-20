class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """ Prefix Sum: O(n), O(1)
        Continously compare running leftSum and rightSum
        """
        left = 0
        total = sum(nums)

        # Edge case: leftSum = rightSum = 0 (pivot = 0)
        if total - nums[0] == 0:
            return 0

        for i in range(1, len(nums)):
            left += nums[i - 1]
            right = total - nums[i] - left
            if left == right:
                return i
        return -1