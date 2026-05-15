class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        Time complexity: O(n) 
        """
        low = 0                  # index of last 0, init = 0
        mid = 0                  # index of current unchecked element, init = start
        high = len(nums) - 1     # index of first 1, init = end
        
        # Loop ends when mid > high. All elements before mid are 0 and 1, all elements from high are 2
        while mid <= high:
            # If current element = 0, swap to the end of "0 region". Then move forward to next unchecked element
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1   # All elements before low = 0
                mid += 1   # All elements before mid are checked, so move forward
            
            # If current element = 1, leave it since 1 must be at the middle, need not to swap.
            elif nums[mid] == 1:
                mid += 1
            
            # Else, current element = 2 , swap it to the end of "2 region"
            else:  
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1 
                # Do not increment mid since swapped element not yet checked
        
        return nums

