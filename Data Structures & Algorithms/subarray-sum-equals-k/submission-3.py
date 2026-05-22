class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0 : 1}    # count of all prefix sum (init empty sum = 0, count 1)
        total = 0               # current sum
        count = 0               # return this

        # If diff = cur_sum - k already in hash map, 
        # cur_sum - diff is count as 1 satisified subarray
        # then add cur_sum to hash map
        for num in nums:
            total += num
            diff = total - k
            
            if diff in prefix_sum:
                count += prefix_sum[diff]
            prefix_sum[total] = prefix_sum.get(total, 0) + 1    # update the count of total as one prefix_sum in map
        return count

        