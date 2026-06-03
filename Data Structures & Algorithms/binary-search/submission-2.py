class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time complexity: O(logn)
        # Space complexity: O(1)
        
        left = 0
        right = len(nums) - 1

        # Loop stops when left > right but still can't find target
        # Thus, return -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            # Search left half if nums[mid] > target
            elif nums[mid] > target:
                right = mid - 1
            
            # Search right hald if nums[mid] < target
            else: 
                left = mid + 1

        return -1
        