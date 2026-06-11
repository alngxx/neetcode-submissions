class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ Brute force:
        1. Merge two arrays into one sorted array
        2. If (m + n) is odd, return mid element
        3. Else (m + n) is even, return average of two mid elemnts
        """
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:  
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1   
        res.extend(nums1[i:])
        res.extend(nums2[j:])

        k = len(res)
        if k % 2 == 1:
            return res[k // 2]
        else:
            median = (res[k // 2] + res[k // 2 - 1]) / 2
            return median