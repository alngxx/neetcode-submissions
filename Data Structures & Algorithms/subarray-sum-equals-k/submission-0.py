class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """ Hash Map: O(n) """
        prefix_sum = {0 : 1}     # dict store frequency of prefix sum
        total = 0                # current running sum
        count = 0

        for num in nums:
            total += num                            # running sum
            complement = total - k

            if complement in prefix_sum:                 # check if current subarray == k, i.e. its complement already in prefix_sum
                count += prefix_sum[complement]          # add all matching subarrays

            prefix_sum[total] = prefix_sum.get(total, 0) + 1   # Update count of that prefix sum
        
        return count


        