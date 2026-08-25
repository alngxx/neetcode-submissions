class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ Index marking with negation: O(n), O(1)
        1. For nums[i], negate number at that index abs(nums[i])
        2. Before negation, we check if that index is already < 0
        3. If so, duplicate found: return
        """
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])

            nums[abs(nums[i])] *= -1

        
        