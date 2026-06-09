class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ Binary Search: O(log n)
        - O(n) linear search is trivial
        - Binary Search on index where sorted order breaks - that's min(nums)
        - The minimum is always ≤ nums[r]
        Compare nums[mid] with nums[r]:
        1. nums[mid] > nums[r]: min must be on the right of mid
        2. nums[mid] ≤ nums[r]: min must be mid or to the left of mid
        """
        l, r = 0, len(nums) - 1
        # Loop ends when l == r
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[r]