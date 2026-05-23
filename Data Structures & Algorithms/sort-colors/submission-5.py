class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        Counting Sort: count each color, then overwrite the original array
        Time complexity: O(3n) = O(n)
        Space complexity: O(1)
        """
        count = [0] * 3    # List store count of 0's, 1's, 2's
        for num in nums:
            count[num] += 1

        # Fill first count[0] with 0's
        # Fill next count[1] with 1's
        # Fill last count[2] with 2's
        index = 0
        for i in range(3):
            for _ in range(count[i]):
                nums[index] = i
                index += 1