class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Intuition: Reverse the array
        """
        n = len(nums)
        k %= n    # k might be > n, rotate might be cycle

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return arr
        
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
