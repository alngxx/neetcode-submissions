class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        Time complexity: O(n) 
        """
        count = [0] * 3      # List store count of 0's, 1's, 2's
        for num in nums:
            count[num] += 1
        
        for i in range(count[0]):
            nums[i] = 0
        for j in range(count[0], len(nums) - count[2]):
            nums[j] = 1
        for k in range(count[0] + count[1], len(nums)):
            nums[k] = 2
            


        


