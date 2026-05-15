class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Loop stops when left > right while cant found target
        # Return left as inserted index
        while left <= right:
            mid = left + (right-left) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid - 1
            
            else:
                left = mid + 1

        # Now left > right, or nums[left] > target > nums[right]
        # Thus, left = inseted index
        return left
        
        