class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        
        return 2*sum(set_nums) - sum(nums)