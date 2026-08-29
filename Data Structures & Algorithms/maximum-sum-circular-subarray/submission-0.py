class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """ Kadane's Algorithm: O(n), O(1)
        There are only 2 cases
        1. Non-circular
        - max_sum is in middle
        - use normal Kadane's algorithm
        2. Circular
        - prefix + middle + suffix = total
        - max_sum = prefix + suffix = total - min_sum
        Thus, to maximize max_sum, we need to find min_sum in middle
        """
        total = sum(nums)
        max_sum = cur_max = nums[0]
        min_sum = cur_min = nums[0]

        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)

            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
        
        # edge case: if all negative, total - min_sum = 0 > max_sum
        # thus, return max_sum
        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, total - min_sum)