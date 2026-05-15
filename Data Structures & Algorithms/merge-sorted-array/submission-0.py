class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Intuition:
        Using two pointers, compare the largest remaining elements of nums1 & nums2, 
        placing the bigger one at the end (nums1[k])
        """

        i = m - 1   # points to last valid element of nums1
        j = n - 1   # points to last/largest element of nums2
        k = m + n - 1 # points to last/largest element of the final list

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            
            # k decrease after every placement
            k -= 1
        
        # Insert leftovers of nums2 into nums 1 
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        
        
        