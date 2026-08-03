class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Hash set: O(n) 
        Use a set for O(1) lookups
        """

        set_nums = set(nums)
        # Initially, streak = 0
        streak = 0

        for num in set_nums:
            if (num - 1) not in set_nums:
                # num is the first number of current streak
                length = 1
                while (num + length) in set_nums:
                    length += 1
                # Update streak only after current streak ends i.e. while loop breaks
                streak = max(streak, length)

        return streak
        
        