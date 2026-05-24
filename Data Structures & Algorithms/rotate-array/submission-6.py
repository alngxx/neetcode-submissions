class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """ Modify in-place, do not return anything
        Reverse the whole array, then reverse the first k and the rest separately
        """
        n = len(nums)
        k %= n    # k might be > n, rotate might be cycle

        def reverse(arr, l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return arr
        
        # [1, 2, 3, 4, 5], k = 2
        reverse(nums, 0, n-1)    # [5, 4, 3, 2, 1]
        reverse(nums, 0, k-1)    # [4, 5, 3, 2, 1]
        reverse(nums, k, n-1)    # [4, 5, 1, 2, 3]