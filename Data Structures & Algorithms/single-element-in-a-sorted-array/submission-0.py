class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """ Brute force
        s = set(nums)
        return 2*sum(s) - sum(nums)
        """
        """ Binary Search 
        Before single element: pairs start at (even, odd)
        After single element: pairs start at (odd, even)
        """

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right-left) // 2

            # ensure mid is even, which point to the first of the pair
            if mid % 2 == 1:
                mid -= 1
            
            # If valid pair, move to next pair (increment left + 2)
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            
            # Else pair is broken -> single element is on the left of mid -> make right = mid
            else:
                right = mid
        
        # Loop ends when left == right at single element
        return nums[right]





        


        