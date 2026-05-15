class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        The problem states: Modify nums in-place
        Thus, we move all NOT 'val' elements to the front
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

        
        