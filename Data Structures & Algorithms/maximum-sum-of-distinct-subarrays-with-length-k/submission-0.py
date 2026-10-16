class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """ Variable-size Sliding Window: O(n), O(k)
        1. Expand r, keeping a set and running sum of the window
        2. Shrink l while nums[r] is already in window or the window.size > k
        3. Update only if window size == k
        """
        res = total = 0
        l = 0
        seen = set()

        for r in range(len(nums)):
            while nums[r] in seen or r - l + 1 > k:
                seen.remove(nums[l])
                total -= nums[l]
                l += 1
            seen.add(nums[r])
            total += nums[r]
            # update only subarray size is k
            if r - l + 1 == k:
                res = max(res, total)

        return res