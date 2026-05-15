class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ Sliding Window: O(n)
        1. [l...r] = window can flip at most k 0's
        2. As r moves right: If nums[r] == 0, flip it: k -= 1
        3. If k < 0, we have used too many flips
            - Shrink the window from the left: l += 1
            - If nums[l] == 0, restore one flip: k += 1
        4. Update longest streak of 1s: streak = max(streak, r - l + 1)
            r - l + 1 = window size of all 1's after flipping at most k times
        """
        l = 0
        streak = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            # If use too many flips, shrink window size by 1: l += 1
            while k < 0:
                # If nums[l] == 0, restore one flip then remove it
                if nums[l] == 0:
                    k += 1
                l += 1
            streak = max(streak, r - l + 1)
        return streak

        