class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # min capacity (best case) = max package
        # max capacity (worse case) = sum of all packages
        l, r = max(weights), sum(weights)     
        res = r

        def can_ship(capacity):
            # cur = current capacity for this day
            # ship_day = day count to ship
            ship_day, cur = 1, capacity     

            for weight in weights:
                if cur - weight < 0:        # package does not fit in current day
                    ship_day += 1           # need a new day
                    if ship_day > days:
                        return False
                    cur = capacity          # reset capacity for the new day

                cur -= weight               # load package onto current day, minus capacity on this day
            return True
        
        while l <= r:
            mid = (l + r) // 2

            # If can ship with capacity = mid, update and search for smaller capacity if possible
            if can_ship(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res