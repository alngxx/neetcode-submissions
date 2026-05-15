class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Missing number = (Sum of 0 -> n) - (Sum of nums)
        # We can define sum function by ourselves

        def sum_list(list):
            res = 0
            for i in list:
                res += i
            return res

        n = len(nums)
        total = n*(n+1) // 2     # /2 will return float type

        return total - sum_list(nums)        