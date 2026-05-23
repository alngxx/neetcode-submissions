class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        Counting Sort: count each color, then overwrite the original array
        - Fill the first count[0] positions with 0.
        - Fill the next count[1] positions with 1.
        - Fill the remaining count[2] positions with 2
        Time complexity: O(n)
        Space complexity: O(1) 
        """
        count = [0] * 3      # List of three store count of 0's, 1's, 2's
        for num in nums:
            count[num] += 1
        
        # Overwrite the array
        for i in range(count[0]):
            nums[i] = 0
        for j in range(count[0], len(nums) - count[2]):
            nums[j] = 1
        for k in range(count[0] + count[1], len(nums)):
            nums[k] = 2