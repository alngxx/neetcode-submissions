class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(arr):
            l, r = 0, len(arr) - 1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return arr
        
        reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])
