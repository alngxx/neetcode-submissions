class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur = 0                    # current window sum
        shortest = float('inf')    # positive infinity

        for r in range(len(nums)):
            cur += nums[r]       # current window's sum

            # while current window's sum still >= target, update its min length before sliding 
            while cur >= target:
                length = r - l + 1
                shortest = min(shortest, length)
                # slide window to the right while keep its sum >= target
                cur -= nums[l]
                l += 1
        
        # For loop ends when iterate all elements. If the whole array's sum < target i.e. shortest still = infinity 
        # => return 0
        if shortest == float('inf'):
            return 0
        else:
            return shortest






        