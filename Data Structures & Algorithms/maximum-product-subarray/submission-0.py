class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)         # max product so far
        cur_max = cur_min = 1   # max and min product ending at i
        
        for i in nums:
            # Save cur_max = previous max * current before updating
            temp = cur_max * i

            # Max is either: keep multiplying, use cur_min (if i negative), or start fresh i
            cur_max = max(temp, cur_min * i, i)

            # Min tracks most negative products that could become max later
            cur_min = min(temp, cur_min * i, i)

            res = max(res, cur_max)   # Update max product 
        return res
        