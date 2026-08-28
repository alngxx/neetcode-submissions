class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """ Simple Binary Search: O(log n)
        1. If nums[mid] > nums[mid + 1]: peak is mid, or on the left
        2. Else nums[mid] < num[mid + 1]: peak is to the right
        3. Since we keep narrow down to find peak in between l..r every step
        4. When l == r, it's peak
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l