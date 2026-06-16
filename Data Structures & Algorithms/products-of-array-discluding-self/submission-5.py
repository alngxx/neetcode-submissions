class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ Prefix + Suffix: O(n)
        res[i] = prefix[i] * suffix[i]
        Store the prefix/suffix first, then update it for next element's
        For instance: [1, 2, 3, 4] -- element 3 (i = 2)
        1. res[2] *= 2 i.e. 1 * 2 = 2   (prefix = 2)
        2. res[2] *= 4 i.e. 2 * 4 = 8   (suffix = 4)
        """
        n = len(nums)
        res = [1] * n         # Init return array - all 1's
        prefix = suffix = 1   # For first/last element, its prefix/suffix of course = 1

        # left -> right
        for i in range(n):
            res[i] *= prefix      
            prefix *= nums[i]   # Update prefix for i+1

        # right -> left
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]   # Update suffix for i-1

        return res