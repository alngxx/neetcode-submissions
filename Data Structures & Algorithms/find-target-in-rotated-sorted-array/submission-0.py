class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Binary Search twice:
        1. Find the index of the break point (minimum) (LeetCode 153)
        2. Decide which halve has target, perform Binary Search on it
        """
        # 1. Find index of min(nums)
        l, r = 0, len(nums) - 1
        while l < r:       
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        minimum = l    # l = r = minimum
        l, r = 0, len(nums) - 1

        # 2. Decide which halve has target
        if target >= nums[minimum] and target <= nums[r]:
            l = minimum
        else:
            r = minimum - 1
        
        # Then, binary search on that halve
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1