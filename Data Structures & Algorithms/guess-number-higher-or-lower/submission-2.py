# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2
            res = guess(mid)     # the API returns 0, -1, or 1

            if res < 0:          # our guess > pick
                r = mid - 1
            elif res > 0:        # our guess < pick
                l = mid + 1
            else:                # our guess = pick
                return mid