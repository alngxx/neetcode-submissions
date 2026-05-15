class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0   # Next position for even numbers
        for j in range(len(nums)):
            if nums[j] % 2 == 0:
                # When an even is found, swap it to the front. Move i forwards for next even number's position
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            # Else if current number is odd, i pointer remains at its position, waiting for being swapped.
        return nums