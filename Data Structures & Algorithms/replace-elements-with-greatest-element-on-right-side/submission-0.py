class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Intuition: O(n)
        - Update max_right as we scan backwards - max_right = greatest element on the right so far
        - So we do not to scan twice to find max, which is O(n^2)
        """

        n = len(arr)
        res = [-1] * n
        max_right = -1

        # Replace res backwards (from index n-1 to 0)
        # Update max_right = greatest element to the right so far
        for i in range(n-1, -1, -1):
            res[i] = max_right
            max_right = max(arr[i], max_right)

        return res


        
        