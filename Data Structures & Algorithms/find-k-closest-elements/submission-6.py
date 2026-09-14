class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """ Two Pointers: O(n-k)
        Since the array is already sorted, 
        use two pointers to shrink to range of k elements
        """
        l, r = 0, len(arr) - 1
        # While loop breaks when (l-r = k-1), keep the range exactly k elements
        while r - l >= k:
            # "<=" matters here since if |a - x| == |b - x| and a < b, keep a
            if abs(arr[l] - x) <= abs(arr[r] - x):
                r -= 1
            else:
                l += 1
        
        # k closest elements, from index l -> r
        return arr[l : r + 1]