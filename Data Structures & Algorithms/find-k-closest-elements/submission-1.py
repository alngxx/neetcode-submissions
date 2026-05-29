class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ Two Pointers: O(n-k)
        Since the array is sorted, can use two pointers to find the range of k elements
        """
        l, r = 0, len(arr) - 1

        # While loop break when (r - l = k - 1), keep the range exactly = k
        while r - l >= k:
            if abs(x - arr[l]) > abs(x - arr[r]):
                l += 1
            else: 
                r -= 1
        
        return arr[l : r+1]

        


        