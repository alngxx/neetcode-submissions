class Solution:
    def check(self, nums: List[int]) -> bool:
        """ Sorted array must only have:
        1. 1 break and tail < head (rotated)
        2. 0 break and tail > head (original)
        Otherwise if array has >= 2 break, invalid
        """
        n = len(nums)
        if n <= 1:
            return True

        break_count = 0
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                break_count += 1
            if break_count >= 2:
                return False        # >= 2 break, array is not sorted

        # check if has one break but tail > head, array is not sorted
        if break_count == 1 and nums[0] < nums[-1]:
            return False

        return True