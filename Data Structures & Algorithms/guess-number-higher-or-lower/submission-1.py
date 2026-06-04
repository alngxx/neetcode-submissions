# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # n is the number we guess at first
        l = 1
        r = n

        while l <= r:
            # At each step, we guess the middle of the range
            mid = (l + r) // 2

            # Call guess(mid) to check our guess > or < pick
            res = guess(mid)
            
            if res < 0:     # pick < num
                r = mid - 1

            elif res > 0:  # pick > num
                l = mid + 1
            
            # Return the pick number, now equal to mid
            else:
                return mid
        