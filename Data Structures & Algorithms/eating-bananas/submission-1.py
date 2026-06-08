class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)  # Search range: min speed 1, max speed = largest pile
        res = r               # Worst case answer: eat fastest pile in 1 hour

        while l <= r:
            k = (l + r) // 2  # Try the middle speed

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / k)  # Hours needed for this pile at speed k
            
            if totalTime <= h:   # Speed k is fast enough — try slower (minimize k)
                res = k
                r = k - 1
            else:                # Too slow — need to eat faster
                l = k + 1

        return res  # Minimum valid k found