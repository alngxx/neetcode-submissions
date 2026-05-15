class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1st solution: O(n)
        # set_nums = set(nums)
        # return 2*sum(set_nums) - sum(nums)

        ''' 2nd solution: Using ^
        XOR of two same numbers is 0. 
        Since all numbers appear twice except one, XOR the whole array gives the single number
        '''

        res = 0 
        # XOR the whole array 
        # Initially, 0 ^ num = num
        for num in nums:
            res = res ^ num
        return res
