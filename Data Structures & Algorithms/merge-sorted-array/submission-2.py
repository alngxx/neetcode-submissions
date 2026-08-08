class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """ Two Pointers: O(n), O(1)
        Do not return anything, modify nums1 in-place instead.
        1. Compare the last 2 elements of two arrays
        2. Place the larger at the end of nums1
        """
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # insert leftovers of nums2 (if there is)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1