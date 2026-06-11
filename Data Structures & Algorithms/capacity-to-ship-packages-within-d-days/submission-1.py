class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:  
        # Check if can ship within days with capacity = cap
        def can_ship(cap):
            # cur = remaining capacity left for the current day's ship
            # count = how many days so far, start = 1
            count, cur = 1, cap

            for w in weights:
                if cur - w < 0:         # package does not fit current day
                    count += 1          # need a new day
                    if count > days:
                        return False
                    cur = cap           # reset capacity for next day since today is full

                cur -= w                # load package onto current day, update remaining capacity
            return True
        
        # min capacity (best case) = max package
        # max capacity (worse case) = sum of all packages
        l, r = max(weights), sum(weights)     
        res = r

        while l <= r:
            mid = (l + r) // 2

            # if can ship with capacity = mid, update capacity, search for smaller one
            if can_ship(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res