class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        Find k largest satisfies: k(k+1)/2 <= n
        => Binary Search: O(log n)
        """
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            total = mid * (mid+1) // 2

            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1
        return right




        