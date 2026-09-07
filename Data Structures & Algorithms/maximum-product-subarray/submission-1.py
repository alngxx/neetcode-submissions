class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """ Kadane's Algorithm: O(n), O(1)
        cur_min = most negative product so far (if exists)
        cur_max is either:
        1. cur_max * num: if num is positive
        2. cur_min * num: if num is negative
        3. fresh num
        """
        res = max(nums)         
        cur_max = cur_min = 1   
        
        for num in nums:
            temp = cur_max * num

            # cur_max is either: keep multiply, cur_min * num (if num < 0), or start fresh
            cur_max = max(temp, cur_min * num, num)

            # cur_min = most negative product that could become max later
            cur_min = min(temp, cur_min * num, num)

            res = max(res, cur_max)
        return res
        