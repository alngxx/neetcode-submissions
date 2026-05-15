class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0   # Track current streak of 1's
        res = 0     # Track highest streak so far

        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            
            if count > res:
                res = count
        return res

        