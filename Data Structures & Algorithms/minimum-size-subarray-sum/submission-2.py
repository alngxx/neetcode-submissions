class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """ Sliding Window: O(n)
        - We track current sum of window: cur_sum
        - While sliding it, keep cur_sum >= target 
        and update shortest window size 
        """
        l = 0
        cur_sum = 0                 # current window sum
        shortest = float('inf')     # infinity

        for r in range(len(nums)):
            cur_sum += nums[r]

            # while window sum >= target, update its min length before sliding
            while cur_sum >= target:
                shortest = min(shortest, r - l + 1)
                
                # slide window while keeps its sum >= target
                cur_sum -= nums[l]
                l += 1
        
        # Edge case: no subarray found (cur_sum never >= target), 
        # thus shortest still = float('inf), return 0
        if shortest == float('inf'):
            return 0
        
        return shortest