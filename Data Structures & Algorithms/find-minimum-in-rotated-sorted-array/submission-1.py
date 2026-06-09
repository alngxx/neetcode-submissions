class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ Binary Search: O(log n)
        - O(n) linear search is trivial
        - Binary Search on the break point - that's min(nums)
        - The minimum is always ≤ nums[r]
        Compare nums[mid] with nums[r]: [3, 4, 5, 6, 1, 2]
        1. nums[mid] > nums[r]: the break point is after mid since ascending order break
        2. nums[mid] ≤ nums[r]: the break point is mid, or before mid
        """
        l, r = 0, len(nums) - 1
        # Loop ends when l == r
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1         # search break point on the right of mid
            else:
                r = mid             # search break point on the left of mid

        return nums[r]