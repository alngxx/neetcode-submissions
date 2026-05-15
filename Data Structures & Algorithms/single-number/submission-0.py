class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        nums.sort()

        # Check if single number either first or last element
        if nums[0] != nums[1]:
            return nums[0]

        elif nums[-1] != nums[-2]:
            return nums[-1]
        
        # If current number different from its two adjacents, return it
        else:
            for i in range(n):
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]

