# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # n is the number we guess at first
        L = 1
        R = n

        while L <= R:
            # At each step, we guess the middle of the range
            mid = (L + R) // 2

            # Call guess(mid) to check our guess > or < pick
            res = guess(mid)

            # If our guess too large, R = mid - 1
            if res < 0:     # pick < num
                R = mid - 1

            elif res > 0:  # pick > num
                L = mid + 1
            
            # Return the pick number, now equal to mid
            else:
                return mid
        