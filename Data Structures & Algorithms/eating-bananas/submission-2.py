class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)   # k search range: min speed = 1, max speed = largest pile
        res = r                # worse case: max speed

        while l <= r:
            mid = (l + r) // 2 # try mid speed

            total_time = 0     # total eating time
            for p in piles:
                total_time += math.ceil(p / mid)  # ceil, not floor: k = 2, need 2 hours to eat 5 piles, not 1
            
            # if total eating time <= h: satisfy, update res
            if total_time <= h:
                res = mid
                r = mid - 1     # try smaller
            else:
                l = mid + 1     # if not satisfy, search larger k

        return res
