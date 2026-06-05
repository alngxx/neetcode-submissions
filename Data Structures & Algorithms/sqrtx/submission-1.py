class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x

        while l <= r:
            mid = l + (r-l) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square <= x:
                l = mid + 1
            else:
                r = mid - 1
        
        # While loop break when l > r but can't find square root
        # Now, r is the largest that r² ≤ x
        # But, l is the smallest that l² > x
        return r