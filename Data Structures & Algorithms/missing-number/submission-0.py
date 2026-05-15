class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Missing number = (Sum of 0 -> n) - (Sum of nums)

        n = len(nums)
        total = n*(n+1) // 2     # /2 will return float type

        return total - sum(nums)        