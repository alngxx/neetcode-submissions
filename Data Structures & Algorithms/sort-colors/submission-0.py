class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []
        for i in nums:
            if i == 0: red.append(i)
            elif i == 1: white.append(i)
            else: blue.append(i)
        
        # Concatenate three lists into one new list in order
        res = red + white + blue

        # Copy res into nums
        for i in range(len(nums)):
            nums[i] = res[i]
        