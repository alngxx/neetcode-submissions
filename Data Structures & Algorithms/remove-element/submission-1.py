class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        The problem states: Modify nums in-place
        Thus, we swap all NOT 'val' elements to the front
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                # If current number != val, increment k
                nums[k] = nums[i]
                k += 1
        return k

        
        