class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use additional array
        n = len(nums)
        res = [0] * n
        
        # For example: res[0 + 3] = nums[0] = 1
        for i in range(n):
            res[(i + k) % n] = nums[i]
        
        nums[:] = res    # Copy nums = res